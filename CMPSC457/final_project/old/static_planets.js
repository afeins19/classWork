// ---- shader setup ----
const vertexShaderSource = `
    attribute vec3 aPosition;
    uniform mat4 uModelViewMatrix;
    uniform mat4 uProjectionMatrix;

    void main() {
        gl_Position = uProjectionMatrix * uModelViewMatrix * vec4(aPosition, 1.0);
    }
`;

const fragmentShaderSource = `
    precision mediump float;
    uniform vec3 uColor;

    void main() {
        gl_FragColor = vec4(uColor, 1.0);
    }
`;

// ---- setup canvas and webgl context ----
const canvas = document.getElementById("webglCanvas");
const gl = canvas.getContext("webgl");

if (!gl) {
    alert("WebGL not supported");
    throw new Error("WebGL not supported");
}

canvas.width = window.innerWidth;
canvas.height = window.innerHeight;
gl.viewport(0, 0, canvas.width, canvas.height);

gl.clearColor(0, 0, 0, 1);
gl.enable(gl.DEPTH_TEST);

// ---- compile shader function ----
function compileShader(source, type) {
    const shader = gl.createShader(type);
    gl.shaderSource(shader, source);
    gl.compileShader(shader);
    if (!gl.getShaderParameter(shader, gl.COMPILE_STATUS)) {
        console.error(type === gl.VERTEX_SHADER ? "Vertex" : "Fragment", "Shader Error:", gl.getShaderInfoLog(shader));
        throw new Error("Shader compilation failed");
    }
    return shader;
}

// ---- create shaders ----
const vertexShader = compileShader(vertexShaderSource, gl.VERTEX_SHADER);
const fragmentShader = compileShader(fragmentShaderSource, gl.FRAGMENT_SHADER);

// ---- create and link program ----
const program = gl.createProgram();
gl.attachShader(program, vertexShader);
gl.attachShader(program, fragmentShader);
gl.linkProgram(program);

if (!gl.getProgramParameter(program, gl.LINK_STATUS)) {
    console.error("Shader program link error:", gl.getProgramInfoLog(program));
    throw new Error("Shader linking failed");
}

gl.useProgram(program);

// ---- create sphere geometry ----
function createSphere(radius, latBands, longBands) {
    const vertices = [];
    const indices = [];
    for (let lat = 0; lat <= latBands; lat++) {
        const theta = (lat * Math.PI) / latBands;
        const sinTheta = Math.sin(theta);
        const cosTheta = Math.cos(theta);

        for (let lon = 0; lon <= longBands; lon++) {
            const phi = (lon * 2 * Math.PI) / longBands;
            const sinPhi = Math.sin(phi);
            const cosPhi = Math.cos(phi);

            const x = cosPhi * sinTheta;
            const y = cosTheta;
            const z = sinPhi * sinTheta;

            vertices.push(radius * x, radius * y, radius * z);
        }
    }

    for (let lat = 0; lat < latBands; lat++) {
        for (let lon = 0; lon < longBands; lon++) {
            const first = lat * (longBands + 1) + lon;
            const second = first + longBands + 1;

            indices.push(first, second, first + 1);
            indices.push(second, second + 1, first + 1);
        }
    }

    return { vertices: new Float32Array(vertices), indices: new Uint16Array(indices) };
}

const sphereData = createSphere(1, 30, 30);

// create vertex buffer
const positionBuffer = gl.createBuffer();
gl.bindBuffer(gl.ARRAY_BUFFER, positionBuffer);
gl.bufferData(gl.ARRAY_BUFFER, sphereData.vertices, gl.STATIC_DRAW);

// create index buffer
const indexBuffer = gl.createBuffer();
gl.bindBuffer(gl.ELEMENT_ARRAY_BUFFER, indexBuffer);
gl.bufferData(gl.ELEMENT_ARRAY_BUFFER, sphereData.indices, gl.STATIC_DRAW);

// get attribute and uniform locations
const aPosition = gl.getAttribLocation(program, "aPosition");
const uModelViewMatrix = gl.getUniformLocation(program, "uModelViewMatrix");
const uProjectionMatrix = gl.getUniformLocation(program, "uProjectionMatrix");
const uColor = gl.getUniformLocation(program, "uColor");

if (aPosition === -1 || !uModelViewMatrix || !uProjectionMatrix || !uColor) {
    throw new Error("Failed to get shader attribute or uniform locations");
}

gl.enableVertexAttribArray(aPosition);
gl.vertexAttribPointer(aPosition, 3, gl.FLOAT, false, 0, 0);

// ---- set up matrices ----
const projectionMatrix = mat4.create();
mat4.perspective(projectionMatrix, Math.PI / 4, canvas.width / canvas.height, 0.1, 100.0);

// ---- define objects ----
const planets = [
    { radius: 1, orbitRadius: 5, orbitSpeed: 0.01, color: [1.0, 0.0, 0.0], position: { x: 0, z: 0 } },
    { radius: 0.5, orbitRadius: 8, orbitSpeed: 0.02, color: [0.0, 0.0, 1.0], position: { x: 0, z: 0 } },
];

// ---- render loop ----
function updateOrbit(planet, time) {
    const angle = time * planet.orbitSpeed;
    planet.position.x = planet.orbitRadius * Math.cos(angle);
    planet.position.z = planet.orbitRadius * Math.sin(angle);
}

function render(time) {
    gl.clear(gl.COLOR_BUFFER_BIT | gl.DEPTH_BUFFER_BIT);

    // Render planets
    planets.forEach((planet) => {
        updateOrbit(planet, time / 1000);

        const modelViewMatrix = mat4.create();
        mat4.translate(modelViewMatrix, modelViewMatrix, [planet.position.x, 0, planet.position.z]);
        mat4.scale(modelViewMatrix, modelViewMatrix, [planet.radius, planet.radius, planet.radius]);

        gl.uniformMatrix4fv(uModelViewMatrix, false, modelViewMatrix);
        gl.uniformMatrix4fv(uProjectionMatrix, false, projectionMatrix);
        gl.uniform3fv(uColor, planet.color);

        gl.drawElements(gl.TRIANGLES, sphereData.indices.length, gl.UNSIGNED_SHORT, 0);
    });

    requestAnimationFrame(render);
}

render();

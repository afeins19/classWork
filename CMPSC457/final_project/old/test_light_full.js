// vertex shader
const vertexShaderSource = `
    attribute vec3 aPosition;
    uniform mat4 uModelViewMatrix;
    uniform mat4 uProjectionMatrix;
    uniform vec3 uLightDirection;

    varying vec3 vNormal;
    varying vec3 vLightDirection;

    void main() {
        vNormal = normalize(aPosition);
        vLightDirection = normalize(uLightDirection);
        gl_Position = uProjectionMatrix * uModelViewMatrix * vec4(aPosition, 1.0);
    }
`;

// fragment shader
const fragmentShaderSource = `
    precision mediump float;

    varying vec3 vNormal;
    varying vec3 vLightDirection;

    uniform vec3 uColor;
    uniform bool uIsAtmosphere;
    uniform bool uIsSun;

    void main() {
        if (uIsSun) {
            gl_FragColor = vec4(uColor, 1.0); // sun always fully illuminated
        } else {
            float diffuse = max(dot(vNormal, vLightDirection), 0.0);
            if (uIsAtmosphere) {
                float intensity = 1.0 - diffuse;
                gl_FragColor = vec4(uColor, 0.2 + 0.3 * intensity);
            } else {
                gl_FragColor = vec4(uColor * diffuse, 1.0);
            }
        }
    }
`;

// setup canvas and webgl context
const canvas = document.getElementById("webglCanvas");
const gl = canvas.getContext("webgl");
if (!gl) {
    alert("webgl not supported");
    throw new Error("webgl not supported");
}

canvas.width = window.innerWidth;
canvas.height = window.innerHeight;
gl.viewport(0, 0, canvas.width, canvas.height);
gl.clearColor(0, 0, 0, 1);
gl.enable(gl.DEPTH_TEST);

// compile shader
function compileShader(source, type) {
    const shader = gl.createShader(type);
    gl.shaderSource(shader, source);
    gl.compileShader(shader);
    if (!gl.getShaderParameter(shader, gl.COMPILE_STATUS)) {
        console.error(gl.getShaderInfoLog(shader));
        throw new Error("shader compile failed");
    }
    return shader;
}

// link shaders to program
const vertexShader = compileShader(vertexShaderSource, gl.VERTEX_SHADER);
const fragmentShader = compileShader(fragmentShaderSource, gl.FRAGMENT_SHADER);
const program = gl.createProgram();
gl.attachShader(program, vertexShader);
gl.attachShader(program, fragmentShader);
gl.linkProgram(program);
if (!gl.getProgramParameter(program, gl.LINK_STATUS)) {
    console.error(gl.getProgramInfoLog(program));
    throw new Error("shader link failed");
}
gl.useProgram(program);

// create sphere geometry
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

// setup buffers
const positionBuffer = gl.createBuffer();
gl.bindBuffer(gl.ARRAY_BUFFER, positionBuffer);
gl.bufferData(gl.ARRAY_BUFFER, sphereData.vertices, gl.STATIC_DRAW);

const indexBuffer = gl.createBuffer();
gl.bindBuffer(gl.ELEMENT_ARRAY_BUFFER, indexBuffer);
gl.bufferData(gl.ELEMENT_ARRAY_BUFFER, sphereData.indices, gl.STATIC_DRAW);

// get locations for uniforms and attributes
const aPosition = gl.getAttribLocation(program, "aPosition");
const uModelViewMatrix = gl.getUniformLocation(program, "uModelViewMatrix");
const uProjectionMatrix = gl.getUniformLocation(program, "uProjectionMatrix");
const uLightDirection = gl.getUniformLocation(program, "uLightDirection");
const uColor = gl.getUniformLocation(program, "uColor");
const uIsAtmosphere = gl.getUniformLocation(program, "uIsAtmosphere");
const uIsSun = gl.getUniformLocation(program, "uIsSun");

gl.enableVertexAttribArray(aPosition);
gl.vertexAttribPointer(aPosition, 3, gl.FLOAT, false, 0, 0);

// setup matrices
const projectionMatrix = mat4.create();
mat4.perspective(projectionMatrix, Math.PI / 4, canvas.width / canvas.height, 0.1, 100.0);

// setup lighting
const lightDirection = [-1.0, 0.0, -1.0];

// define celestial objects
const celestialBodies = [
    {
        type: "sun",
        radius: 1.0,
        position: [0, 0, 0],
        color: [1.0, 1.0, 0.0],
        isSun: true,
    },
    {
        type: "planet",
        radius: 0.6,
        orbitRadius: 5,
        orbitSpeed: 0.01,
        color: [0.0, 0.0, 1.0],
        hasAtmosphere: true,
        moons: [
            {
                radius: 0.15,
                orbitRadius: 1.2,
                orbitSpeed: 0.05,
                color: [0.6, 0.6, 0.6],
                position: { x: 0, z: 0 },
            },
        ],
        position: { x: 0, z: 0 },
    },
    {
        type: "planet",
        radius: 0.5,
        orbitRadius: 8,
        orbitSpeed: 0.007,
        color: [1.0, 0.0, 0.0],
        hasAtmosphere: true,
        moons: [
            {
                radius: 0.2,
                orbitRadius: 1.5,
                orbitSpeed: 0.03,
                color: [0.8, 0.8, 0.8],
                position: { x: 0, z: 0 },
            },
        ],
        position: { x: 0, z: 0 },
    },
];

// update orbits
function updateOrbits(time) {
    celestialBodies.forEach((body) => {
        if (body.type === "planet") {
            const angle = time * body.orbitSpeed;
            body.position.x = body.orbitRadius * Math.cos(angle);
            body.position.z = body.orbitRadius * Math.sin(angle);

            body.moons.forEach((moon) => {
                const moonAngle = time * moon.orbitSpeed;
                moon.position.x = body.position.x + moon.orbitRadius * Math.cos(moonAngle);
                moon.position.z = body.position.z + moon.orbitRadius * Math.sin(moonAngle);
            });
        }
    });
}

// render loop
function render(time) {
    gl.clear(gl.COLOR_BUFFER_BIT | gl.DEPTH_BUFFER_BIT);

    updateOrbits(time / 1000);

    celestialBodies.forEach((body) => {
        const modelViewMatrix = mat4.create();
        mat4.translate(modelViewMatrix, modelViewMatrix, [body.position.x || 0, 0, body.position.z || 0]);
        mat4.scale(modelViewMatrix, modelViewMatrix, [body.radius, body.radius, body.radius]);

        gl.uniformMatrix4fv(uModelViewMatrix, false, modelViewMatrix);
        gl.uniformMatrix4fv(uProjectionMatrix, false, projectionMatrix);
        gl.uniform3fv(uLightDirection, lightDirection);
        gl.uniform3fv(uColor, body.color);
        gl.uniform1i(uIsSun, body.isSun || false);
        gl.uniform1i(uIsAtmosphere, false);
        gl.drawElements(gl.TRIANGLES, sphereData.indices.length, gl.UNSIGNED_SHORT, 0);

        // render atmosphere
        if (body.hasAtmosphere && !body.isSun) {
            const atmosphereMatrix = mat4.create();
            mat4.translate(atmosphereMatrix, atmosphereMatrix, [body.position.x || 0, 0, body.position.z || 0]);
            mat4.scale(atmosphereMatrix, atmosphereMatrix, [body.radius * 1.2, body.radius * 1.2, body.radius * 1.2]);

            gl.uniformMatrix4fv(uModelViewMatrix, false, atmosphereMatrix);
            gl.uniform1i(uIsAtmosphere, true);
            gl.uniform3fv(uColor, [0.2, 0.4, 1.0]);
            gl.drawElements(gl.TRIANGLES, sphereData.indices.length, gl.UNSIGNED_SHORT, 0);
        }

        // render moons
        if (body.moons) {
            body.moons.forEach((moon) => {
                const moonMatrix = mat4.create();
                mat4.translate(moonMatrix, moonMatrix, [moon.position.x, 0, moon.position.z]);
                mat4.scale(moonMatrix, moonMatrix, [moon.radius, moon.radius, moon.radius]);

                gl.uniformMatrix4fv(uModelViewMatrix, false, moonMatrix);
                gl.uniform1i(uIsAtmosphere, false);
                gl.uniform3fv(uColor, moon.color);
                gl.drawElements(gl.TRIANGLES, sphereData.indices.length, gl.UNSIGNED_SHORT, 0);
            });
        }
    });

    requestAnimationFrame(render);
}

render();

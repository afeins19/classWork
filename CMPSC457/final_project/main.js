// ---- shader setup ----
const vertexShaderSource = `
attribute vec3 aPosition;
varying vec3 vFragmentPosition;
uniform mat4 uModelViewMatrix;
uniform mat4 uProjectionMatrix;
uniform mat4 uNormalMatrix;
uniform vec3 uSunPosition; // position of the sun

varying vec3 vNormal;
varying vec3 vLightDir;

void main() {
    // transofrm the normal using the normal matrix
    vNormal = normalize(vec3(uNormalMatrix * vec4(aPosition, 0.0)));

    // get light direction: (sun - fragment)
    vec3 fragmentPosition = vec3(uModelViewMatrix * vec4(aPosition, 1.0));
    vLightDir = normalize(uSunPosition - fragmentPosition);


    
    // Project the vertex position
    gl_Position = uProjectionMatrix * uModelViewMatrix * vec4(aPosition, 1.0);
}

`;

const fragmentShaderSource = `
precision mediump float;

varying vec3 vNormal;
varying vec3 vLightDir;

uniform vec3 uColor;         // Base color of the object
uniform vec3 uCameraPosition; // Camera position
uniform bool uIsSun;         // Is the object the sun?



void main() {
    if (uIsSun) {
        // Sun is fully bright
        gl_FragColor = vec4(uColor, 1.0);
    } else {
        // Normalize inputs
        vec3 normal = normalize(vNormal);
        vec3 lightDir = normalize(vLightDir);
        vec3 viewDir = normalize(uCameraPosition); // direction from fragment to camera

        // Ensure the backside of the planet is fully dark
        if (dot(normal, lightDir) <= 0.0) {
            gl_FragColor = vec4(0.0, 0.0, 0.0, 1.0); // full dark
            return;
        }

        // diffuse lighting: ensure only the front side gets lighting
        float diffuse = max(dot(normal, lightDir), 0.0);

        // Ambient lighting: apply only to the lit side
        float ambient = 0.2;

        // Specular lighting: subtle highlights on the lit side
        vec3 reflectDir = reflect(-lightDir, normal);
        float specularStrength = 0.3;
        float spec = pow(max(dot(viewDir, reflectDir), 0.0), 50.0) * diffuse; // Specular tied to diffuse
        vec3 specular = vec3(1.0) * spec * specularStrength;

        // Combine lighting
        vec3 lighting = uColor * (diffuse + ambient) + specular;

        gl_FragColor = vec4(lighting, 1.0);
    }
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

// ******************** SIMULATION PARAMS ********************
const MAX_RENDER_DISTANCE = 700;
const G = 9.81 
const STARS = generateStars(500, 500);
// ***********************************************************


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

// ---- light setup ----
const sunPosition = [0.0, 0.0, 0.0]; 
const uSunPosition = gl.getUniformLocation(program, "uSunPosition");
const uCameraPosition = gl.getUniformLocation(program, "uCameraPosition");

gl.uniform3fv(uSunPosition, sunPosition);


// ---- create sphere geometry ----
function createSphere(radius, latBands, longBands) {
    const vertices = [];
    const indices = [];

    // generates spehres by drawing bands along latitude and longitude
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
            
            // all bands are represented by vertices that are joined in the frag shader
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

// uniform, normal, projection matrices
const aPosition = gl.getAttribLocation(program, "aPosition");
const uModelViewMatrix = gl.getUniformLocation(program, "uModelViewMatrix");
const uNormalMatrix = gl.getUniformLocation(program, "uNormalMatrix");
const uProjectionMatrix = gl.getUniformLocation(program, "uProjectionMatrix");
const uColor = gl.getUniformLocation(program, "uColor");

gl.enableVertexAttribArray(aPosition);
gl.vertexAttribPointer(aPosition, 3, gl.FLOAT, false, 0, 0);

// ---- set up matrices ----
const projectionMatrix = mat4.create();
mat4.perspective(projectionMatrix, Math.PI / 4, canvas.width / canvas.height, 0.1, MAX_RENDER_DISTANCE);

// ---- simulation speed ----
let simulationRate = 1.0;

document.getElementById("increaseRate").addEventListener("click", () => {
    simulationRate += 1; // increase simulation speed
    console.log("Simulation rate increased to:", simulationRate);
});

document.getElementById("decreaseRate").addEventListener("click", () => {
    simulationRate = Math.max(0.5, simulationRate - 1); // decrease simulation speed
    console.log("Simulation rate decreased to:", simulationRate);
});

// ---- spawn meteors ----
document.getElementById("spawnMeteorButton").addEventListener("click", () => {
    spawnMeteor();
});

// ---- camera setup ----
const camera = {
    position: [0, 100, 200],
    speed: 0.3,
};
const keys = {};

window.addEventListener("keydown", (e) => keys[e.key] = true);
window.addEventListener("keyup", (e) => keys[e.key] = false);

function updateCamera() {
    if (keys["w"]) camera.position[2] -= camera.speed; // forward
    if (keys["s"]) camera.position[2] += camera.speed; // backward
    if (keys["a"]) camera.position[0] -= camera.speed; // left
    if (keys["d"]) camera.position[0] += camera.speed; // right
    if (keys["q"]) camera.position[1] += camera.speed; // up
    if (keys["e"]) camera.position[1] -= camera.speed; // down
}

// ---- define celestial bodies ----
const celestialBodies = [
    {
        type: "sun",
        radius: 10, 
        position: [0, 0, 0],
        color: [1.0, 1.0, 0.0], // yellow
    },
    
    {
        type: "planet",
        radius: 1,
        orbitRadius: 15,
        orbitSpeed: 0.1,
        color: [1.0, 0.0, 0.0], // red
        position: { x: 0, z: 0 },
    },

    {
        type: "planet",
        radius: 4,
        orbitRadius: 55,
        orbitSpeed: 0.05,
        color: [0.0, 0.4, 0.8], // light blue
        position: { x: 0, z: 0 },

        moons: [
            {
                radius: 0.15,
                orbitRadius: 2,
                orbitSpeed: 0.075,
                color: [0.8, 0.8, 0.8], // gray
                position: { x: 0, z: 0 },
            },
        ],
    },

    {
        type: "planet",
        radius: 2,
        orbitRadius: 95,
        orbitSpeed: 0.04,
        color: [0.4, 0.2, 0.6], // purple
        position: { x: 0, z: 0 },
    },
    
    {
        type: "planet",
        radius: 5,
        orbitRadius: 125,
        orbitSpeed: 0.02,
        color: [0.6, 0.3, 0.0], // brown
        position: { x: 0, z: 0 },

        moons: [
            {
                radius: 0.15,
                orbitRadius: 2,
                orbitSpeed: 0.35,
                color: [0.8, 0.8, 0.8], // gray
                position: { x: 0, z: 0 },
            },

            {
                radius: 0.15,
                orbitRadius: 3.5,
                orbitSpeed: 0.05,
                color: [0.5, 0.2, 0.2], // red-gray
                position: { x: 1, z: 1 },
            },

            
        ],
    },
];



// ---- define asteroid belt ----
const asteroidBelt = [];
const asteroidCount = 2000;

for (let i = 0; i < asteroidCount; i++) {
    const angle = Math.random() * Math.PI * 2; // rand angle
    const distance = 200 + Math.random() * 10; // random distance from sun
    
    asteroidBelt.push({
        type: "asteroid",
        radius: 0.1 + Math.random() * 0.3, // small random size
        orbitRadius: distance,
        orbitSpeed: 0.1 + Math.random() * 0.05, // random orbit speed
        angle: angle,
        color: [0.5 + Math.random() * 0.05, 0.5 + Math.random() * 0.05, 0.5 + Math.random() * 0.05], 
        position: { x: distance * Math.cos(angle), z: distance * Math.sin(angle) },
    });
}

const meteors = [];
const meteorCount = 20;

// --------- RANDOM METEORS ---------
for (let i = 0; i < meteorCount; i++) {
    const angle = Math.random() * Math.PI * 2;
    const distance = 100 + Math.random() * 20; // start far from planets
    meteors.push({
        type: "meteor",
        position: {
            x: distance * Math.cos(angle),
            y: (Math.random() - 0.5) * 20, // random height
            z: distance * Math.sin(angle),
        },
        velocity: {
            x: (Math.random() - 0.5) * 0.5, // random velocity
            y: (Math.random() - 0.5) * 0.5,
            z: (Math.random() - 0.5) * 0.5,
        },
        radius: 0.2,
        color: [0.8, 0.4, 0.1], // brownish
    });
}

function spawnMeteor() {
    const randomAngle = Math.random() * 2 * Math.PI; // random direction
    const spawnDistance = 150; // distance from the center to spawn meteors

    // random position far from the center
    const startX = Math.cos(randomAngle) * spawnDistance;
    const startZ = Math.sin(randomAngle) * spawnDistance;

    const meteor = {
        position: { x: startX, y: 0, z: startZ },
        velocity: { x: Math.random() * 0.5 , y: 0, z: Math.random() * 0.5  }, 
        radius: Math.random() * 0.5 + .25 , // random radius between 0.1 and 0.6
        color: [0.8, 0.4, 0.1], // brownish
    };

    meteors.push(meteor); // Add the new meteor to the array
    console.log("Meteor spawned @ :", meteor.position);
}

function initOrbits(){
    celestialBodies.forEach((body) => {
        if (body.type === "planet" || body.type === "moon") {
            const angle = time * body.orbitSpeed * simulationRate * (Math.random * 2 * pi);
            body.position.x = body.orbitRadius * Math.cos(angle);
            body.position.z = body.orbitRadius * Math.sin(angle);

            // update moons relative to their planet
            if (body.moons) {
                body.moons.forEach((moon) => {
                    const moonAngle = time * moon.orbitSpeed * simulationRate;
                    moon.position.x = body.position.x + moon.orbitRadius * Math.cos(moonAngle);
                    moon.position.z = body.position.z + moon.orbitRadius * Math.sin(moonAngle);
                });
            }
        }
    });
    
}


function updateOrbits(time) {
    const damping = 0.6; // damping factor to slow down meteors

    // update planets and moons
    celestialBodies.forEach((body) => {
        if (body.type === "planet" || body.type === "moon") {
            const angle = time * body.orbitSpeed * simulationRate;
            body.position.x = body.orbitRadius * Math.cos(angle);
            body.position.z = body.orbitRadius * Math.sin(angle);

            // update moons relative to their planet
            if (body.moons) {
                body.moons.forEach((moon) => {
                    const moonAngle = time * moon.orbitSpeed * simulationRate;
                    moon.position.x = body.position.x + moon.orbitRadius * Math.cos(moonAngle);
                    moon.position.z = body.position.z + moon.orbitRadius * Math.sin(moonAngle);
                });
            }
        }
    });

    // update meteors
    for (let i = meteors.length - 1; i >= 0; i--) {
        const meteor = meteors[i];

        // check gravitational pull and collisions for meteors
        celestialBodies.forEach((body) => {
            if (body.type === "planet" || body.type === "moon") {
                // calculate direction vector (planet -> meteor)
                const dx = body.position.x - meteor.position.x;
                const dy = (body.position.y || 0) - meteor.position.y; // use 0 if body.position.y is undefined
                const dz = body.position.z - meteor.position.z;
                const distance = Math.sqrt(dx * dx + dy * dy + dz * dz);

                // add gravitational pull
                if (distance > 1.0) { // avoid singularities at very close distances
                    const force = G / (distance * distance); // gravity ~ 1/d^2
                    meteor.velocity.x += force * dx / distance;
                    meteor.velocity.y += force * dy / distance;
                    meteor.velocity.z += force * dz / distance;
                }

                // check for collision
                if (distance < body.radius + meteor.radius) {
                    console.log(`[COLLISION] METEOR -> ${body.type}!`);
                    meteors.splice(i, 1); // remove meteor from the array
                    return; // skip further updates for this meteor
                }
            }
        });

        // apply damping to slow down meteors
        meteor.velocity.x *= damping;
        meteor.velocity.y *= damping;
        meteor.velocity.z *= damping;

        // update meteor position after applying gravity and damping
        meteor.position.x += meteor.velocity.x;
        meteor.position.y += meteor.velocity.y;
        meteor.position.z += meteor.velocity.z;
    }

    // update asteroid belt
    asteroidBelt.forEach((asteroid) => {
        asteroid.angle += asteroid.orbitSpeed * simulationRate * 0.01; // increment angle for orbit
        asteroid.position.x = asteroid.orbitRadius * Math.cos(asteroid.angle);
        asteroid.position.z = asteroid.orbitRadius * Math.sin(asteroid.angle);
    });
}


function updateCamera() {
    if (keys["w"]) camera.position[2] -= camera.speed; //  forward
    if (keys["s"]) camera.position[2] += camera.speed; //  backward
    if (keys["a"]) camera.position[0] -= camera.speed; //  left
    if (keys["d"]) camera.position[0] += camera.speed; //  right
    if (keys["q"]) camera.position[1] += camera.speed; //  up
    if (keys["e"]) camera.position[1] -= camera.speed; //  down
}

// random  position stars
function generateStars(numStars, radius) {
    const stars = [];
    for (let i = 0; i < numStars; i++) {
        const x = (Math.random() - 0.5) * radius * 2; 
        const y = (Math.random() - 0.5) * radius * 2; 
        const z = (Math.random() - 0.5) * radius * 2; 
        stars.push({ x, y, z });
    }
    return stars;
}

const stars= generateStars(10000,500)

function renderStars() {
    stars.forEach((star) => {
        const modelViewMatrix = mat4.create();
        mat4.translate(modelViewMatrix, modelViewMatrix, [star.x, star.y, star.z]);
        mat4.scale(modelViewMatrix, modelViewMatrix, [0.1, 0.1, 0.1]); // small size for stars

        gl.uniformMatrix4fv(uModelViewMatrix, false, modelViewMatrix);
        gl.uniform3fv(uColor, [0.75, 0.75, 0.75]); // darker stars

        gl.drawElements(gl.POINTS, sphereData.indices.length, gl.UNSIGNED_SHORT, 0);
    });
}


function render(time) {
    gl.clear(gl.COLOR_BUFFER_BIT | gl.DEPTH_BUFFER_BIT);

    updateCamera();
    updateOrbits(time / 1000);

    renderStars();

    // render celestial bodies
    celestialBodies.forEach((body) => {
        const modelViewMatrix = mat4.create();
        mat4.lookAt(modelViewMatrix, camera.position, [0, 0, 0], [0, 1, 0]);
        mat4.translate(modelViewMatrix, modelViewMatrix, [body.position.x || 0, 0, body.position.z || 0]);
        mat4.scale(modelViewMatrix, modelViewMatrix, [body.radius, body.radius, body.radius]);

        gl.uniformMatrix4fv(uModelViewMatrix, false, modelViewMatrix);

        const normalMatrix = mat4.create();
        mat4.invert(normalMatrix, modelViewMatrix);
        mat4.transpose(normalMatrix, normalMatrix);
        gl.uniformMatrix4fv(uNormalMatrix, false, normalMatrix);

        gl.uniformMatrix4fv(uProjectionMatrix, false, projectionMatrix);
        gl.uniform3fv(uColor, body.color);

        gl.uniform1i(gl.getUniformLocation(program, "uIsSun"), body.type === "sun");

        gl.drawElements(gl.TRIANGLES, sphereData.indices.length, gl.UNSIGNED_SHORT, 0);

        // render moons
        if (body.moons) {
            body.moons.forEach((moon) => {
                const moonModelViewMatrix = mat4.create();
                mat4.translate(
                    moonModelViewMatrix,
                    modelViewMatrix,
                    [moon.position.x - body.position.x, 0, moon.position.z - body.position.z]
                );
                mat4.scale(moonModelViewMatrix, moonModelViewMatrix, [moon.radius, moon.radius, moon.radius]);

                gl.uniformMatrix4fv(uModelViewMatrix, false, moonModelViewMatrix);
                gl.uniform3fv(uColor, moon.color);

                gl.drawElements(gl.TRIANGLES, sphereData.indices.length, gl.UNSIGNED_SHORT, 0);
            });
        }
    });

    // render asteroid belt
    asteroidBelt.forEach((asteroid) => {
        const modelViewMatrix = mat4.create();
        mat4.lookAt(modelViewMatrix, camera.position, [0, 0, 0], [0, 1, 0]);
        mat4.translate(modelViewMatrix, modelViewMatrix, [asteroid.position.x, 0, asteroid.position.z]);
        mat4.scale(modelViewMatrix, modelViewMatrix, [asteroid.radius, asteroid.radius, asteroid.radius]);

        gl.uniformMatrix4fv(uModelViewMatrix, false, modelViewMatrix);
        gl.uniform3fv(uColor, asteroid.color);

        gl.uniform1i(gl.getUniformLocation(program, "uIsSun"), false);

        gl.drawElements(gl.TRIANGLES, sphereData.indices.length, gl.UNSIGNED_SHORT, 0);
    });

    // render meteors
    meteors.forEach((meteor) => {
        const modelViewMatrix = mat4.create();
        mat4.lookAt(modelViewMatrix, camera.position, [0, 0, 0], [0, 1, 0]);
        mat4.translate(modelViewMatrix, modelViewMatrix, [meteor.position.x, meteor.position.y, meteor.position.z]);
        mat4.scale(modelViewMatrix, modelViewMatrix, [meteor.radius, meteor.radius, meteor.radius]);
    
        gl.uniformMatrix4fv(uModelViewMatrix, false, modelViewMatrix);
        gl.uniform3fv(uColor, meteor.color);
    
        gl.uniform1i(gl.getUniformLocation(program, "uIsSun"), false);
    
        gl.drawElements(gl.TRIANGLES, sphereData.indices.length, gl.UNSIGNED_SHORT, 0);
    });

    requestAnimationFrame(render);
}

render();

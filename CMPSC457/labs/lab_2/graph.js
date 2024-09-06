// Get the canvas element from the HTML file and set up the WebGL context
const canvas = document.getElementById('webgl-canvas');

// Set canvas size to 50% of the window
canvas.width = window.innerWidth * 0.5;
canvas.height = window.innerHeight * 0.5;

const gl = canvas.getContext('webgl');

// Check if WebGL is supported
if (!gl) {
    console.error("WebGL not supported!");
}

// Function to set the background color based on multiple color conditions
function setBackground(index) {
    const colors = [
        [0.0, 0.0, 0.0, 1.0], // Black
        [0.0, 0.5, 0.5, 1.0], // Teal
        [0.5, 0.0, 0.5, 1.0], // Purple
        [0.0, 0.0, 0.5, 1.0], // Dark Blue
    ];
    const chosenColor = colors[index % colors.length];
    gl.clearColor(...chosenColor); // Clear the background with the chosen color
    gl.clear(gl.COLOR_BUFFER_BIT); // Clear the color buffer
}

// Function to draw points at different locations, sizes, and colors
function drawPoint(x, y, size, color) {
    const vertices = new Float32Array([x, y]);
    const buffer = gl.createBuffer();
    gl.bindBuffer(gl.ARRAY_BUFFER, buffer);
    gl.bufferData(gl.ARRAY_BUFFER, vertices, gl.STATIC_DRAW);

    const vertexShaderSource = `
        attribute vec2 coordinates;
        void main(void) {
            gl_PointSize = ${size.toFixed(1)};
            gl_Position = vec4(coordinates, 0.0, 1.0);
        }
    `;
    const fragmentShaderSource = `
        void main(void) {
            gl_FragColor = vec4(${color.join(',')});
        }
    `;
    
    const vertexShader = gl.createShader(gl.VERTEX_SHADER);
    gl.shaderSource(vertexShader, vertexShaderSource);
    gl.compileShader(vertexShader);

    const fragmentShader = gl.createShader(gl.FRAGMENT_SHADER);
    gl.shaderSource(fragmentShader, fragmentShaderSource);
    gl.compileShader(fragmentShader);

    const shaderProgram = gl.createProgram();
    gl.attachShader(shaderProgram, vertexShader);
    gl.attachShader(shaderProgram, fragmentShader);
    gl.linkProgram(shaderProgram);
    gl.useProgram(shaderProgram);

    const coord = gl.getAttribLocation(shaderProgram, "coordinates");
    gl.enableVertexAttribArray(coord);
    gl.bindBuffer(gl.ARRAY_BUFFER, buffer);
    gl.vertexAttribPointer(coord, 2, gl.FLOAT, false, 0, 0);
    
    gl.drawArrays(gl.POINTS, 0, 1);
}

// Define the positions, sizes, and colors of the points
const points = [
    { x: -0.5, y: 0.5, size: 10.0, color: [1.0, 0.0, 0.0, 1.0] }, // Red
    { x: 0.5, y: 0.5, size: 20.0, color: [0.0, 1.0, 0.0, 1.0] },  // Green
    { x: -0.5, y: -0.5, size: 30.0, color: [0.0, 0.0, 1.0, 1.0] }, // Blue
    { x: 0.5, y: -0.5, size: 40.0, color: [1.0, 1.0, 0.0, 1.0] }, // Yellow
    { x: 0.0, y: 0.0, size: 50.0, color: [1.0, 0.0, 1.0, 1.0] }  // Magenta
];

// Function to render the scene
function renderScene() {
    // Alternate between background colors for demo purposes
    const backgroundIndex = Math.floor(Math.random() * 4);
    setBackground(backgroundIndex);

    // Draw each point with its specific position, size, and color
    points.forEach(point => {
        drawPoint(point.x, point.y, point.size, point.color);
    });
}

// Continuously render the scene
function animate() {
    renderScene();
    requestAnimationFrame(animate);
}

// Start the animation
animate();

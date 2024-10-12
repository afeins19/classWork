// context setup - grabs canvas from HTML
const canvas = document.getElementById('canvas');
const gl = canvas.getContext('webgl'); // setup rendering context for the canvas

canvas.width = window.innerWidth;
canvas.height = window.innerHeight;

// fixing sizing issue - synching up canvas with actual screen size
gl.viewport(0, 0, canvas.width, canvas.height);

// setting up vertex shader - handles positions and colors
const vertexShaderSource = `
    attribute vec2 position;
    attribute vec4 aColor;
    varying vec4 vColor;
    void main() {
        gl_Position = vec4(position, 0.0, 1.0);
        vColor = aColor; // Pass color to fragment shader
    }
`;

// setting up fragment shader - handles color of each pixel
const fragmentShaderSource = `
    precision mediump float;
    varying vec4 vColor;
    void main() {
        gl_FragColor = vColor; // Set the fragment color to the passed color
    }
`;

// creates shaders
function generateShader(source, type) {
    const shader = gl.createShader(type);
    gl.shaderSource(shader, source); // gives source code from WebGL
    gl.compileShader(shader); // compiles WebGL

    // Check for shader compilation errors
    if (!gl.getShaderParameter(shader, gl.COMPILE_STATUS)) {
        console.error('Shader compile failed: ' + gl.getShaderInfoLog(shader));
        return null;
    }
    return shader;
}

function main(vertexSource, fragmentSource) {
    const vertexShader = generateShader(vertexSource, gl.VERTEX_SHADER); // creating vertex shader object
    const fragmentShader = generateShader(fragmentSource, gl.FRAGMENT_SHADER); // same but frag

    const program = gl.createProgram();
    gl.attachShader(program, vertexShader);
    gl.attachShader(program, fragmentShader);
    gl.linkProgram(program);

    if (!gl.getProgramParameter(program, gl.LINK_STATUS)) {
        console.error('Program failed to link: ' + gl.getProgramInfoLog(program));
        return null;
    }

    return program;
}

// ------------------------------------------------------------------------------------------------------
// run program

const program = main(vertexShaderSource, fragmentShaderSource);
gl.useProgram(program);

// scales the vertices for visibility
function scaleVertex(v, factor, offset) {
    return [(v[0] * factor) + offset[0], (v[1] * factor) + offset[1]];
}

// gets the midpoint b/w 2 vertices
function getMidPoint(a, b) {
    const mp_x = (a[0] + b[0]) / 2;
    const mp_y = (a[1] + b[1]) / 2;

    return [mp_x, mp_y];
}

// generates vertices to make Sierpienski triangle
function makeSerpienski(a, b, c, i, vertices, colors, scale, offset) {
    // base case - just plot the triangle
    if (i == 0) {
        // scaling points up otherwise triangles are too small to see
        a = scaleVertex(a, scale, offset);
        b = scaleVertex(b, scale, offset);
        c = scaleVertex(c, scale, offset);
        
        

        const color = [Math.random(), Math.random(), Math.random(), 1.0];
        colors.push(...color, ...color, ...color); // add color for each vertex

        // adding x, y coordinates for each triangle
        vertices.push(a[0], a[1], b[0], b[1], c[0], c[1]);
    } else {
        const mid_ab = getMidPoint(a, b);
        const mid_bc = getMidPoint(b, c);
        const mid_ac = getMidPoint(a, c);

        i--;

        // recursively subdivide triangles
        makeSerpienski(a, mid_ab, mid_ac, i, vertices, colors, scale, offset); // left triangle
        makeSerpienski(mid_ab, b, mid_bc, i, vertices, colors, scale, offset); // center triangle
        makeSerpienski(mid_ac, mid_bc, c, i, vertices, colors, scale, offset); // right triangle
    }
}

// calculating the number of triangles - using the geometric series
function countTriangles(recursions) {
    count = (1 + (Math.pow(3, recursions + 1) - 3) / 2);
    return count;
}

// ------------------------------------------------------------------------------------------------------
// PARAMETERS

let recursion_depth = 0; // inital recursion depth
const scale = 1;
const offset = [0.0, 0.0];
const v_start = [[-0.5, -0.5], [0.5, -0.5], [0.0, 0.5]]; // initial vertices

// Draw fractal based on recursion depth
function drawFractal() {
    const vertices = [];
    const colors = []; // Colors array updated dynamically during recursion

    // call recursive function to generate vertices and colors
    makeSerpienski(v_start[0], v_start[1], v_start[2], recursion_depth, vertices, colors, scale, offset);

    // Update data vals in the HTML
    const num_triangles = countTriangles(recursion_depth);
    document.getElementById('num_triangles').innerText = num_triangles;
    document.getElementById('recursion_depth').innerText = recursion_depth;
    // ------------------------------------------------------------------------------------------------------
    // BUFFER SETUP

    // bubfr for vertices
    const buffer = gl.createBuffer();
    gl.bindBuffer(gl.ARRAY_BUFFER, buffer);
    gl.bufferData(gl.ARRAY_BUFFER, new Float32Array(vertices), gl.STATIC_DRAW);

    const positionLocation = gl.getAttribLocation(program, 'position'); // gets the position from the vertex shader
    gl.enableVertexAttribArray(positionLocation); // enable position attribute
    gl.vertexAttribPointer(positionLocation, 2, gl.FLOAT, false, 0, 0); // set up the attribute pointer

    // buffer for colors
    const colorBuffer = gl.createBuffer();
    gl.bindBuffer(gl.ARRAY_BUFFER, colorBuffer);
    gl.bufferData(gl.ARRAY_BUFFER, new Float32Array(colors), gl.STATIC_DRAW);

    const colorLocation = gl.getAttribLocation(program, 'aColor'); // gets colors from the vertex shader
    gl.enableVertexAttribArray(colorLocation);
    gl.vertexAttribPointer(colorLocation, 4, gl.FLOAT, false, 0, 0); // colors are vec4 (RGBA)

    gl.clear(gl.COLOR_BUFFER_BIT);
    gl.drawArrays(gl.TRIANGLES, 0, vertices.length / 2);
}

// ------------------------------------------------------------------------------------------------------
// BUTTON CONTROLS
document.getElementById('increase').addEventListener('click', () => {
        recursion_depth++;
        drawFractal(); 
});

document.getElementById('decrease').addEventListener('click', () => {
    if (recursion_depth >= 0) {
        recursion_depth--;
        drawFractal(); 
    }
});

// first draw
drawFractal();

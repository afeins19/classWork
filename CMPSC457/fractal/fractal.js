// context setup - grabs canvas from html
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
    // creating general shader object
    const vertexShader = generateShader(vertexSource, gl.VERTEX_SHADER); // creating vertex shader object
    const fragmentShader = generateShader(fragmentSource, gl.FRAGMENT_SHADER); // same but frag 
    
    // linking all the shaders into a single webgl program 
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
function scaleVertex(v, factor, offset){
    return [(v[0] * factor) + offset[0], (v[1] * factor) + offset[1]];
}

// gets the midpoint b/w 2 vertices
function getMidPoint(a, b) {
    const mp_x = (a[0] + b[0]) / 2;
    const mp_y = (a[1] + b[1]) / 2;

    return [mp_x, mp_y]; 
}

// generates vertices to make serpienski triangle 
// a = left, b = center , c = right  
function makeSerpienski(a, b, c, i, vertices, scale, offset) {
    // base case - just plot the triangle 
    if (i == 0) {
        // scaling points up otherwise triangles are too small to see 
        a = scaleVertex(a, scale, offset);
        b = scaleVertex(b, scale, offset); 
        c = scaleVertex(c, scale, offset);  

        const color = [(Math.random() * i), (Math.random() * i), (Math.random() * i), 1.0];
        colors.push(...color, ...color, ...color); // add color for each vertex

        // adding x,y coordinates for each triangle 
        vertices.push(a[0], a[1], b[0], b[1], c[0], c[1]);
    } 
    // recursive case - generating points for next triangle recursion 
    else {
        const mid_ab = getMidPoint(a, b);
        const mid_bc = getMidPoint(b, c);
        const mid_ac = getMidPoint(a, c);

        i--; 

        // recursively subdivide triangles
        makeSerpienski(a, mid_ab, mid_ac, i, vertices, scale, offset); // left triangle
        makeSerpienski(mid_ab, b, mid_bc, i, vertices, scale, offset); // center triangle 
        makeSerpienski(mid_ac, mid_bc, c, i, vertices, scale, offset); // right triangle 
    }
}

// ------------------------------------------------------------------------------------------------------
// PARAMETERS 

const vertices = [];
const colors = [];
const recursion_depth = 2;  
const scale = 1; 
const offset = [0.0, 0.0]; 
const v_start = [[-0.5, -0.5], [0.5, -0.5], [0.0, 0.5]]; // initial vertices 

// call recursive function
makeSerpienski(v_start[0], v_start[1], v_start[2], recursion_depth, vertices, scale, offset, colors); 
// ------------------------------------------------------------------------------------------------------
// BUFFER STUFF 

const buffer = gl.createBuffer(); 
gl.bindBuffer(gl.ARRAY_BUFFER, buffer); 
gl.bufferData(gl.ARRAY_BUFFER, new Float32Array(vertices), gl.STATIC_DRAW); 

const positionLocation = gl.getAttribLocation(program, 'position'); // gets the position from the vertex shader 
gl.enableVertexAttribArray(positionLocation); // enable position attribute
gl.vertexAttribPointer(positionLocation, 2, gl.FLOAT, false, 0, 0); // set up the attribute pointer


const colorBuffer = gl.createBuffer();
gl.bindBuffer(gl.ARRAY_BUFFER, colorBuffer);
gl.bufferData(gl.ARRAY_BUFFER, new Float32Array(colors), gl.STATIC_DRAW);

const colorLocation = gl.getAttribLocation(program, 'aColor'); // gets colors from the vertex shader
gl.enableVertexAttribArray(colorLocation);
gl.vertexAttribPointer(colorLocation, 4, gl.FLOAT, false, 0, 0); // colors are vec4 (RGBA)

// ------------------------------------------------------------------------------------------------------
// RENDERING 

function render() {
    gl.clear(gl.COLOR_BUFFER_BIT);
    gl.drawArrays(gl.TRIANGLES, 0, vertices.length / 2);
    requestAnimationFrame(render); 
}

// launch 
render();

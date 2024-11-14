// --- canvas setup ---

const canvas = document.getElementById("webgl");
const gl = canvas.getContext("webgl");

if (!gl) {
    console.log("Failed to get the WebGL rendering context.");
}

// --- vertex shader setup ---
// new matrices for calculating viewability of vertices 
const VSHADER_SOURCE = `
    attribute vec4 a_Position;
    attribute vec4 a_Color;
    uniform mat4 u_ModelMatrix;
    uniform mat4 u_ViewMatrix;
    uniform mat4 u_ProjectionMatrix;
    varying vec4 v_Color;
    void main() {
        gl_Position = u_ProjectionMatrix * u_ViewMatrix * u_ModelMatrix * a_Position;
        v_Color = a_Color;
    }`;


// --- fragment shader setup --
const FSHADER_SOURCE = `
    precision mediump float;
    varying vec4 v_Color;
    void main() {
        gl_FragColor = v_Color;
    }
`;

// --- main ---
function main() {

    if (!initShaders(gl, VSHADER_SOURCE, FSHADER_SOURCE)) {
        console.log("Failed to initialize shaders.");
        return;
    }

    

    // vertice params: (x,y,z,r,g,b)
    const vertices = new Float32Array([
        // black (front) v0-v3
        1, -1, -1, 0, 0, 0,
        1,  1, -1, 0, 0, 0,
        1,  1,  1, 0, 0, 0,
        1, -1,  1, 0, 0, 0,
        
        // pink (right) v4-v7
        1, -1, -1, 1, 0, 1,
        1,  1, -1, 0, 0, 0,
        1,  1,  1, 1, 0, 1,
        1, -1,  1, 0, 0, 0,
        
        // pink (left) v8-v11
        -1, -1, -1, 1, 0, 1,
        -1,  1, -1, 0, 0, 0,
        -1,  1,  1, 1, 0, 1,
        -1, -1,  1, 0, 0, 0,
    
        // light blue (back) v12-v15
        -1, -1, -1, 0, 1, 1,
         1, -1, -1, 0, 0, 0,
         1,  1, -1, 0, 1, 1,
        -1,  1, -1, 0, 0, 0,
        
        // yellow (bottom) v16-v19
        -1, -1, -1, 1, 1, 0,
        -1, -1,  1, 0, 0, 0,
         1, -1,  1, 1, 1, 0,
         1, -1, -1, 0, 0, 0,
        
        // yellow (top) v20-v23
        -1,  1, -1, 1, 1, 0,
        -1,  1,  1, 0, 0, 0,
         1,  1,  1, 1, 1, 0,
         1,  1, -1, 0, 0, 0,
        
        // INNER TRIANGLE (multi color) v24-v25
        -0.75,  0.25, -0.75, .5, .5, 1,
        -0.75, -0.25, -0.75, .5, .5, 1,
         0.5,  -0.5,  -0.75, 1, .5, .5,


        0.5,  0.25, -0.75, 0, 0, 0,
        0.5, 0.25, 0,0, 0, 0,
        -0.5,  0.25,  -0.75, 0, 0, 0,
        0.5,  0.25,  0, 0, 0, 0
         
    ]);
    


    // determines order of how vertices are drawn in the traingles 
    const indices = new Uint8Array([
        0, 1, 2, 0, 2, 3,           // back
        4, 5, 6, 4, 6, 7,           // front 
        8, 9, 10, 8, 10, 11,        // left 
        12, 13, 14, 12, 14, 15,     // rght 
        16, 17, 18, 16, 18, 19,     // bottom 
        20, 21, 22, 20, 22, 23,     // top 


        // triangle 
        24, 25, 26,

        // inner square
        27,28,29,30
    ]);

    // -- matrix initialization --- 

    const idx_len = indices.length;
    setupBuffer(gl, vertices, indices);


    const u_ModelMatrix = gl.getUniformLocation(gl.program, "u_ModelMatrix");
    const u_ViewMatrix = gl.getUniformLocation(gl.program, "u_ViewMatrix");
    const u_ProjectionMatrix = gl.getUniformLocation(gl.program, "u_ProjectionMatrix");

    // -- viewing params --
    let nearPlane = 0.1; // distance to near plane 
    let rotateAngle = 0; // amount to rotate 

    const modelMatrix = new Matrix4();
    const viewMatrix = new Matrix4();
    const projectionMatrix = new Matrix4();

    // --- key press handling --- 
    document.onkeydown = function (ev) {
        switch (ev.key) { 
            case "ArrowUp": nearPlane += 0.1; break;
            case "ArrowDown": nearPlane = Math.max(0.1, nearPlane - 0.1); break;
            case "ArrowLeft": rotateAngle -= 2; break;
            case "ArrowRight": rotateAngle += 2; break;
        }

        // render after key press 
        render(gl, idx_len, modelMatrix, u_ModelMatrix, viewMatrix, u_ViewMatrix, projectionMatrix, u_ProjectionMatrix, nearPlane, rotateAngle);
    };

    
    // -- binding position and vertex data --
    function setupBuffer(gl, vertices, indices) {
        const squareBuffer = gl.createBuffer();
        const idxBuffer = gl.createBuffer();
    
        gl.bindBuffer(gl.ARRAY_BUFFER, squareBuffer);
        gl.bufferData(gl.ARRAY_BUFFER, vertices, gl.STATIC_DRAW);
    
        const FSIZE = vertices.BYTES_PER_ELEMENT;
        const a_Position = gl.getAttribLocation(gl.program, "a_Position");
        const a_Color = gl.getAttribLocation(gl.program, "a_Color");
    
        gl.vertexAttribPointer(a_Position, 3, gl.FLOAT, false, FSIZE * 6, 0);
        gl.enableVertexAttribArray(a_Position);
    
        gl.vertexAttribPointer(a_Color, 3, gl.FLOAT, false, FSIZE * 6, FSIZE * 3);
        gl.enableVertexAttribArray(a_Color);
    
        gl.bindBuffer(gl.ELEMENT_ARRAY_BUFFER, idxBuffer);
        gl.bufferData(gl.ELEMENT_ARRAY_BUFFER, indices, gl.STATIC_DRAW);
    }

    // -- drawing --
    function render(gl, idx_len, modelMatrix, u_ModelMatrix, viewMatrix, u_ViewMatrix, projectionMatrix, u_ProjectionMatrix, nearPlane, rotateAngle) {
        // purge buffers
        gl.clearColor(0.0, 0.0, 0.0, 1.0); // black background
        gl.clear(gl.COLOR_BUFFER_BIT | gl.DEPTH_BUFFER_BIT);
        
        // set matrices responsible for: view, projection, and rotation 
        modelMatrix.setRotate(rotateAngle, 0, 1, 0);
        viewMatrix.setLookAt(0, 0, 5, 0, 0, 0, 0, 1, 0);
        projectionMatrix.setPerspective(45, canvas.width / canvas.height, nearPlane, 100);
        
        // pass matrices to webgl
        gl.uniformMatrix4fv(u_ModelMatrix, false, modelMatrix.elements);
        gl.uniformMatrix4fv(u_ViewMatrix, false, viewMatrix.elements);
        gl.uniformMatrix4fv(u_ProjectionMatrix, false, projectionMatrix.elements);
        
        // render the scene
        gl.drawElements(gl.TRIANGLES, idx_len, gl.UNSIGNED_BYTE, 0);
    }


}

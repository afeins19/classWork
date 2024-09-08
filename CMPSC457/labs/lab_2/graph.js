var VSHADER_SOURCE =
  'attribute vec4 a_Position;\n' +
  'attribute vec4 a_Color;\n' +
  'varying vec4 v_Color;\n' +
  'void main() {\n' +
  '  gl_Position = a_Position;\n' +
  '  gl_PointSize = 200.0;\n' + // Set point size
  '  v_Color = a_Color;\n' +   // Pass color to fragment shader
  '}\n';

// Fragment shader program
var FSHADER_SOURCE =
  'precision mediump float;\n' +
  'varying vec4 v_Color;\n' +
  'void main() {\n' +
  '  gl_FragColor = v_Color;\n' + // Use the varying color
  '}\n';

function main() {
  // Retrieve <canvas> element
  var canvas = document.getElementById('webgl');

  // Get the rendering context for WebGL
  var gl = canvas.getContext('webgl');
  if (!gl) {
    console.log('Failed to get the rendering context for WebGL');
    return;
  }

  // Initialize shaders
  if (!initShaders(gl, VSHADER_SOURCE, FSHADER_SOURCE)) {
    console.log('Failed to initialize shaders.');
    return;
  }

  // Write the positions of vertices and colors to a vertex shader
  var n = initVertexBuffers(gl);
  if (n < 0) {
    console.log('Failed to set the positions of the vertices');
    return;
  }

  // Specify the color for clearing <canvas>
  gl.clearColor(0.0, 0.0, 0.0, 1.0);

  // Clear <canvas>
  gl.clear(gl.COLOR_BUFFER_BIT);

  // Draw the points
  gl.drawArrays(gl.POINTS, 0, n);
}

function initVertexBuffers(gl) {
  var verticesColors = new Float32Array([
    
     0.0,  0.5,  1.0, 0.0, 0.0, 1.0, // red
    -0.5, -0.5,  0.0, 1.0, 0.0, 1.0, // green 
     0.5, -0.5,  0.0, 0.0, 1.0, 1.0  // blue 
  ]);
  var n = 3; // static verticy count

  // buffer obj
  var vertexColorBuffer = gl.createBuffer();
  if (!vertexColorBuffer) {
    console.log('Failed to create the buffer object');
    return -1;
  }

  // Bind 
  gl.bindBuffer(gl.ARRAY_BUFFER, vertexColorBuffer);
  // Write to buffer
  gl.bufferData(gl.ARRAY_BUFFER, verticesColors, gl.STATIC_DRAW);

  var FSIZE = verticesColors.BYTES_PER_ELEMENT;

  // get vertex attributes 
  var a_Position = gl.getAttribLocation(gl.program, 'a_Position');
  if (a_Position < 0) {
    console.log('Failed to get the storage location of a_Position');
    return -1;
  }
  gl.vertexAttribPointer(a_Position, 2, gl.FLOAT, false, FSIZE * 6, 0);
  gl.enableVertexAttribArray(a_Position);

  // set some colors 
  var a_Color = gl.getAttribLocation(gl.program, 'a_Color');
  if (a_Color < 0) {
    console.log('Failed to get the storage location of a_Color');
    return -1;
  }
  gl.vertexAttribPointer(a_Color, 4, gl.FLOAT, false, FSIZE * 6, FSIZE * 2);
  gl.enableVertexAttribArray(a_Color);

  return n;
}
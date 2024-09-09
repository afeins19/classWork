   // Vertex shader program
   var VSHADER_SOURCE =
   'attribute vec4 a_Position;\n' +
   'attribute float a_PointSize;\n' +   // Attribute for point size
   'attribute vec4 a_Color;\n' +        // Attribute for color
   'varying vec4 v_Color;\n' +          // Pass color to fragment shader
   'void main() {\n' +
   '  gl_Position = a_Position;\n' +
   '  gl_PointSize = a_PointSize;\n' +  // Set point size from attribute
   '  v_Color = a_Color;\n' +           // Pass color to fragment shader
   '}\n';

 // Fragment shader program
 var FSHADER_SOURCE =
   'precision mediump float;\n' +       // Specify precision
   'varying vec4 v_Color;\n' +          // Receive color from vertex shader
   'void main() {\n' +
   '  gl_FragColor = v_Color;\n' +      // Set the fragment color
   '}\n';

 function main() {
   // Retrieve <canvas> element
   var canvas = document.getElementById('webglCanvas');

   // Get the rendering context for WebGL
   var gl = getWebGLContext(canvas);
   if (!gl) {
     console.log('Failed to get the rendering context for WebGL');
     return;
   }

   // Initialize shaders
   if (!initShaders(gl, VSHADER_SOURCE, FSHADER_SOURCE)) {
     console.log('Failed to intialize shaders.');
     return;
   }

   // Set up vertex and color buffer
   var n = initVertexBuffers(gl);
   if (n < 0) {
     console.log('Failed to set the positions of the vertices');
     return;
   }

   // Set the background color (split into two halves)
   gl.clearColor(0.8, 0.8, 1.0, 1.0);   // Light blue
   gl.clear(gl.COLOR_BUFFER_BIT);
   
   // Draw the first half (top background)
   gl.clear(gl.COLOR_BUFFER_BIT);       // Clear with background color
   gl.viewport(0, 0, canvas.width, canvas.height / 2);  // Top half
   gl.clearColor(1.0, 0.0, 1.0, 1.0);   // Light blue background
   gl.clear(gl.COLOR_BUFFER_BIT);
   
   // Draw the second half (bottom background)
   gl.viewport(0, canvas.height / 2, canvas.width, canvas.height / 2);
   gl.clearColor(0.0, 0.5, 0.5, 1.0);   // Dark blue background
   gl.clear(gl.COLOR_BUFFER_BIT);

   // Draw the points
   gl.viewport(0, 0, canvas.width, canvas.height);  // Reset viewport to full canvas
   gl.drawArrays(gl.POINTS, 0, n);  // Draw points
 }

 function initVertexBuffers(gl) {
   // Vertex positions, sizes, and colors for 4 points
   var verticesSizesColors = new Float32Array([
     // x, y, size, r, g, b, a
      0.0,  0.5, 150.0,  1.0, 0.0, 0.0, 1.0,  // Red point (top middle)
     -0.5,  0.0,  100.0,  0.0, 1.0, 0.0, 1.0,  // Green point (left middle)
      0.5,  0.0,  50.0,  0.0, 0.0, 1.0, 1.0,  // Blue point (right middle)
      0.0, -0.5,  220.0,  1.0, 1.0, 0.0, 1.0   // Yellow point (bottom middle)
   ]);
   var n = 4; // The number of points

   // Create a buffer object
   var vertexBuffer = gl.createBuffer();
   if (!vertexBuffer) {
     console.log('Failed to create the buffer object');
     return -1;
   }

   // Bind the buffer object to target
   gl.bindBuffer(gl.ARRAY_BUFFER, vertexBuffer);

   // Write data into the buffer object
   gl.bufferData(gl.ARRAY_BUFFER, verticesSizesColors, gl.STATIC_DRAW);

   var FSIZE = verticesSizesColors.BYTES_PER_ELEMENT;

   // Get the storage location of a_Position, assign, and enable
   var a_Position = gl.getAttribLocation(gl.program, 'a_Position');
   if (a_Position < 0) {
     console.log('Failed to get the storage location of a_Position');
     return -1;
   }
   gl.vertexAttribPointer(a_Position, 2, gl.FLOAT, false, FSIZE * 7, 0);
   gl.enableVertexAttribArray(a_Position);  // Enable the assignment of buffer object

   // Get the storage location of a_PointSize, assign, and enable
   var a_PointSize = gl.getAttribLocation(gl.program, 'a_PointSize');
   if (a_PointSize < 0) {
     console.log('Failed to get the storage location of a_PointSize');
     return -1;
   }
   gl.vertexAttribPointer(a_PointSize, 1, gl.FLOAT, false, FSIZE * 7, FSIZE * 2);
   gl.enableVertexAttribArray(a_PointSize);  // Enable the assignment of buffer object

   // Get the storage location of a_Color, assign, and enable
   var a_Color = gl.getAttribLocation(gl.program, 'a_Color');
   if (a_Color < 0) {
     console.log('Failed to get the storage location of a_Color');
     return -1;
   }
   gl.vertexAttribPointer(a_Color, 4, gl.FLOAT, false, FSIZE * 7, FSIZE * 3);
   gl.enableVertexAttribArray(a_Color);  // Enable the assignment of buffer object

   return n;
 }
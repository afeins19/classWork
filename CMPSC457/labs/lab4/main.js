// global vars 
const RESOLUTION = 1000; // circle plotting resolution
const RADIUS = 0.9;

// Vertex shader program
var VSHADER_SOURCE =
  "attribute vec4 a_Position;\n" +
  "void main() {\n" +
  "  gl_Position = a_Position;\n" +
  "  gl_PointSize = 5.0;\n" +
  "}\n";

// Fragment shader program
var FSHADER_SOURCE =
  "precision mediump float;\n" +
  "uniform vec4 u_FragColor;\n" +
  "void main() {\n" +
  "  gl_FragColor = u_FragColor;\n" +
  "}\n";

function main() {
  var canvas = document.getElementById("webgl");

  var gl = getWebGLContext(canvas);
  if (!gl) {
    console.log("Failed to get the rendering context for WebGL");
    return;
  }

  // Shader setup 
  if (!initShaders(gl, VSHADER_SOURCE, FSHADER_SOURCE)) {
    console.log("Failed to intialize shaders.");
    return;
  }

  var a_Position = gl.getAttribLocation(gl.program, "a_Position");
  if (a_Position < 0) {
    console.log("Failed to get the storage location of a_Position");
    return;
  }

  let u_FragColor = gl.getUniformLocation(gl.program, "u_FragColor");
  if (u_FragColor < 0) {
    console.log("Failed to get the storage location of u_FragColor");
    return;
  }

  // Set background 
  gl.clearColor(0.0, 0.0, 0.0, 1.0);

  // Draw clock elements 
  updateClock(gl, a_Position, u_FragColor);

  setInterval(function () {
    updateClock(gl, a_Position, u_FragColor);
  }, 1);
}

// Draws hands & tick marks 
function drawClockElements(gl, unit, pos, radius, len, a_Position) {
  let vertecies = [
    // bottom of tick marks 
    radius * Math.cos(((pos - unit) * Math.PI) / 180),             // inner corner x-coordinate 
    radius * Math.sin(((pos - unit) * Math.PI) / 180),             // inner corner y-coordinate
    (radius + len) * Math.cos(((pos - unit) * Math.PI) / 180),     // outer corner x-coordinate
    (radius + len) * Math.sin(((pos - unit) * Math.PI) / 180),     // outer corner y-coordinate 

    // top of tick marks 
    radius * Math.cos(((pos + unit) * Math.PI) / 180),
    radius * Math.sin(((pos + unit) * Math.PI) / 180),
    (radius + len) * Math.cos(((pos + unit) * Math.PI) / 180),
    (radius + len) * Math.sin(((pos + unit) * Math.PI) / 180),
  ];

  var vertices = new Float32Array(vertecies);
  var n = vertices.length / 2;

  // Buffer object
  var vertexBuffer = gl.createBuffer();
  if (!vertexBuffer) {
    console.log("Failed to create the buffer object");
    return false;
  }

  // Bind to target 
  gl.bindBuffer(gl.ARRAY_BUFFER, vertexBuffer);
  gl.bufferData(gl.ARRAY_BUFFER, vertices, gl.STATIC_DRAW);

  var FSIZE = vertices.BYTES_PER_ELEMENT;
  // Get memory location of a_Position and assign 
  gl.vertexAttribPointer(a_Position, 2, gl.FLOAT, false, FSIZE * 2, 0);
  gl.enableVertexAttribArray(a_Position); // Enable the assignment of the buffer object

  // Unbind
  gl.bindBuffer(gl.ARRAY_BUFFER, null);

  // Draw
  gl.drawArrays(gl.TRIANGLE_STRIP, 0, n);
}

// Move the clock hands to the corresponding time 
function updateClock(gl, a_Position, u_FragColor) {
  // Clear the canvas
  gl.clear(gl.COLOR_BUFFER_BIT);

  // Draw watch face  
  gl.uniform4f(u_FragColor, 1, 1, 1, 1);
  drawWatchFace(gl, a_Position);

  // Drawing tick marks 
  let hr_positions = 360 / 60;
  let tick_unit = 360 / 60;

  for (let i = 0; i < 60; i++) {
    gl.uniform4f(u_FragColor, 0, 0, 0, 1); // Default tick mark color

    // make actual hours pink
    if ((hr_positions * i) % 5 == 0) {
      gl.uniform4f(u_FragColor, 1, 0.35, 0.85, 1);
      drawClockElements(gl, 2, hr_positions * i, RADIUS - 0.15, 0.1, a_Position);

    }

    // draw small tick mark 
    else{
      drawClockElements(gl, 1, hr_positions * i, RADIUS - 0.10, 0.05, a_Position);
    }

  }

  // Getting current time 
  const now = new Date();
  let MILISECONDS = now.getMilliseconds();
  let SECONDS = now.getSeconds();
  let MINUTES = now.getMinutes()-15;
  let HOURS = now.getHours()-2.90;


  // Calculate positions
  let mse_pos = MILISECONDS;
  let sec_pos = SECONDS * tick_unit;
  let min_pos = MINUTES * tick_unit + SECONDS * tick_unit / 60;
  let hrs_pos = (HOURS % 12) * (360 / 12) + MINUTES * (360 / 12) / 60;

  // milliseconds hand
  gl.uniform4f(u_FragColor, .8, .8, .8, 1); // green
  drawClockElements(gl, 2, -mse_pos, 0, 0.7, a_Position);

  // Seconds hand 
  gl.uniform4f(u_FragColor, 1, 0, 0, 1); // Red color
  drawClockElements(gl, 2, -sec_pos, 0, 0.7, a_Position);

  // Minutes hand 
  gl.uniform4f(u_FragColor, 0, 1, 0.8, 1); // Greenish color
  drawClockElements(gl, 2, -min_pos, 0, 0.7, a_Position);

  // Hour hand 
  gl.uniform4f(u_FragColor, 0, 0.6, 1, 1); // Blueish color 
  drawClockElements(gl, 4, -hrs_pos, 0, 0.4, a_Position);
}

function drawWatchFace(gl, a_Position) {
  // Coordinates
  let vertecies = [];

  let get_circle = (i, r, res) => {
    return {
      x: r * Math.cos((i * 2 * Math.PI) / res),
      y: r * Math.sin((i * 2 * Math.PI) / res),
    };
  };

  // Creating frame for the watch face 
  for (let i = 0; i < RESOLUTION; i++) {
    // Create n=RESOLUTION vertices to make up the watch face circle 
    let arc = get_circle(i, RADIUS, RESOLUTION);
    vertecies.push(arc.x, arc.y);
  }
  var vertices = new Float32Array(vertecies);
  var n = vertices.length / 2;

  // Create a buffer object
  var vertexBuffer = gl.createBuffer();
  if (!vertexBuffer) {
    console.log("Failed to create the buffer object");
    return false;
  }

  // Bind the buffer object to target
  gl.bindBuffer(gl.ARRAY_BUFFER, vertexBuffer);
  gl.bufferData(gl.ARRAY_BUFFER, vertices, gl.STATIC_DRAW);

  var FSIZE = vertices.BYTES_PER_ELEMENT;
  // Get the storage location of a_Position, assign and enable buffer
  gl.vertexAttribPointer(a_Position, 2, gl.FLOAT, false, FSIZE * 2, 0);
  gl.enableVertexAttribArray(a_Position); // Enable the assignment of the buffer object

  // Unbind the buffer object
  gl.bindBuffer(gl.ARRAY_BUFFER, null);

  // Draw the circle
  gl.drawArrays(gl.TRIANGLE_FAN, 0, n);
}

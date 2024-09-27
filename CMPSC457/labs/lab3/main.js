// global vars 
const RESOLUTION = 1000; // circle plotting resolution
const RADIUS = .9; 

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

  // shader setup 
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

 
  gl.clearColor(0.0, 0.0, 0.0, 1.0);
  gl.clear(gl.COLOR_BUFFER_BIT);

  // watchface  
  gl.uniform4f(u_FragColor, 1, 1, 1, 1);
  drawWatchFace(gl, a_Position, u_FragColor);

  // seconds hand 
  gl.uniform4f(u_FragColor, 1, 0, 0, 1);
  drawClockElements(gl, 2, 45, 0, .7, a_Position, u_FragColor);

  // minutes hand 
  gl.uniform4f(u_FragColor, 0, 1, .8, 1);
  // draw the minutes clock hand
  drawClockElements(gl, 2, 0, 0, 0.7, a_Position, u_FragColor);

  // set hour clock hand color
  gl.uniform4f(u_FragColor, 0, 1, .8, 1); // blueish green 
  // draw the hour clock hand
  drawClockElements(gl, 4, 90, 0, 0.4, a_Position, u_FragColor);

  // drawing tick marks 
  for (let i = 0; i < 12; i++){
    gl.uniform4f(u_FragColor, 0, 0, 0, 1);

    tick_unit = 360 / 12; 

    // make 12 o'clock mark pink 
    if (((tick_unit * i) * 2 * Math.PI) / 360 == Math.PI / 2) {
      gl.uniform4f(u_FragColor, 1, .35, .85, 1);

    }

    // draw each tick mark 
    drawClockElements(gl, 2, tick_unit * i, RADIUS - 0.15, 0.1, a_Position, u_FragColor);
  }
}

// draws hands & tick marks 
function drawClockElements(gl, unit, pos, radius, len, a_Position) {
  let vertecies = [
    // bottom of tick marks 
    radius * Math.cos(((pos - unit)  * Math.PI) / 180),             // inner corner x-cordinate 
    radius * Math.sin(((pos - unit) * Math.PI) / 180),              // inner corner y-cordinate
    (radius + len) * Math.cos(((pos - unit) * Math.PI) / 180),      // outer corner x-cordinate
    (radius + len) * Math.sin(((pos - unit) * Math.PI) / 180),      // outer corner y-cordinate 

    // top of tick marks 
    radius * Math.cos(((pos + unit) *  Math.PI) / 180),
    radius * Math.sin(((pos + unit) * Math.PI) / 180),
    (radius + len) * Math.cos(((pos + unit) * Math.PI) / 180),
    (radius + len) * Math.sin(((pos + unit) * Math.PI) / 180),
  ];

  var vertices = new Float32Array(vertecies);
  var n = vertices.length / 2;

  // buffer object
  var vertexBuffer = gl.createBuffer();
  if (!vertexBuffer) {
    console.log("Failed to create the buffer object");
    return false;
  }

  // bind to target 
  gl.bindBuffer(gl.ARRAY_BUFFER, vertexBuffer);
  gl.bufferData(gl.ARRAY_BUFFER, vertices, gl.STATIC_DRAW);

  var FSIZE = vertices.BYTES_PER_ELEMENT;
  // get memory location of a_pos and assign 
  gl.vertexAttribPointer(a_Position, 2, gl.FLOAT, false, FSIZE * 2, 0);
  gl.enableVertexAttribArray(a_Position); // Enable the assignment of the buffer object

  // unbind
  gl.bindBuffer(gl.ARRAY_BUFFER, null);

  // draw
  gl.drawArrays(gl.TRIANGLE_STRIP, 0, n);
}

function drawWatchFace(gl, a_Position) {
  // coordinates
  let vertecies = [];

  let get_circle = (i, r, res) => {
    return {
      x: r * Math.cos((i * 2 * Math.PI) / res),
      y: r * Math.sin((i * 2 * Math.PI) / res),
    };
  };

  // creating frame for the watchface 
  for (let i = 0; i < RESOLUTION; i++) {
    // create n=RESOLUTION vertices to make up the watchface circle 
    arc = get_circle(i, RADIUS, RESOLUTION);
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
  //Get the storage location of a_Position, assign and enable buffer
  gl.vertexAttribPointer(a_Position, 2, gl.FLOAT, false, FSIZE * 2, 0);
  gl.enableVertexAttribArray(a_Position); // Enable the assignment of the buffer object

  // Unbind the buffer object
  gl.bindBuffer(gl.ARRAY_BUFFER, null);

  // superimposing traingles over each other to draw a circle 
  gl.drawArrays(gl.TRIANGLE_FAN, 0, n);
}

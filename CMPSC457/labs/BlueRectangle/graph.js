// Lab 2 - Aaron Feinberg

function main() {
    // get the canvas element 
    var canvas = document.getElementById('main_canvas');

    if (!canvas) {
        console.log('Error: No Canvas')
        return; 
    }
    var ctx = canvas.getContext('2d'); 

    ctx.fillStyle = 'rgba(0, 0, 255, 1.0)'; // blue 
    ctx.fillRect(120,10,150,150); // (x,y,h,w)
}
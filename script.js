let isDrowing = false;
let x1 = 0;
let y1 = 0;

const canvas = document.getElementById('c1');
const ctx = canvas.getContext('2d');

canvas.addEventListener('mousedown', event => {
    x1 = event.offsetX;
    y1 = event.offsetY;
    isDrowing = true;
    drawing(ctx, x1, y1, event.offsetX, event.offsetY);
});

canvas.addEventListener('mousemove', event => {
    if (isDrowing === true) {
        drawing(ctx, x1, y1, event.offsetX, event.offsetY);
        x1 = event.offsetX;
        y1 = event.offsetY;
    };
});

window.addEventListener('mouseup', event => {
    if (isDrowing === true) {
        drawing(ctx, x1, y1, event.offsetX, event.offsetY);
        x1 = 0;
        y1 = 0;
        isDrowing = false;
    };
});

function drawing(ctx, x1, y1, x2, y2) {
    ctx.beginPath();
    ctx.strokeStyle = 'white';
    ctx.lineWidth = 30;
    ctx.moveTo(x1, y1);
    ctx.lineTo(x2, y2);
    ctx.stroke();
    ctx.closePath();


    ctx.beginPath();
    ctx.strokeStyle = 1;
    ctx.fillStyle = 'white';
    ctx.arc(x2, y2, 15, 0, 2*Math.PI, false);
    ctx.fill();
    ctx.closePath();
}
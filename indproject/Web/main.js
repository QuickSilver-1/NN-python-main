let isDrowing = false;
let x1 = 0;
let y1 = 0;

const canvas = document.getElementById('c1'),
      ctx = canvas.getContext('2d');

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
    ctx.lineWidth = 24;
    ctx.moveTo(x1, y1);
    ctx.lineTo(x2, y2);
    ctx.stroke();
    ctx.closePath();


    ctx.beginPath();
    ctx.strokeStyle = 1;
    ctx.fillStyle = 'white';
    ctx.arc(x2, y2, 12, 0, 2*Math.PI, false);
    ctx.fill();
    ctx.closePath();
};

eel.expose(gray_format);
function gray_format () {
    const imageData = ctx.getImageData(0, 0, canvas.width, canvas.height);
    const data = imageData.data;
    let img = [];
    for (let i = 0; i < data.length; i += 4) {
        img[img.length] = (data[i] + data[i+1] + data[i+2]) / 3};
        return img
};

function clearing() {
    ctx.clearRect(0, 0, 392, 392);
};

async function call() {
    await eel.go(gray_format());
};

eel.expose(write);
function write (answer) {
    document.getElementById('let').innerHTML = 'Распознанная цифр: ' + answer.indexOf(Math.max(...answer));
    document.getElementById('chance0').innerHTML = '0 - ' + answer[0] + '%';
    document.getElementById('chance1').innerHTML = '1 - ' + answer[1] + '%';
    document.getElementById('chance2').innerHTML = '2 - ' + answer[2] + '%';
    document.getElementById('chance3').innerHTML = '3 - ' + answer[3] + '%';
    document.getElementById('chance4').innerHTML = '4 - ' + answer[4] + '%';
    document.getElementById('chance5').innerHTML = '5 - ' + answer[5] + '%';
    document.getElementById('chance6').innerHTML = '6 - ' + answer[6] + '%';
    document.getElementById('chance7').innerHTML = '7 - ' + answer[7] + '%';
    document.getElementById('chance8').innerHTML = '8 - ' + answer[8] + '%';
    document.getElementById('chance9').innerHTML = '9 - ' + answer[9] + '%';
};




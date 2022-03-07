eel.expose(printer_1)
function printer_1(x) {
    console.log(x);
    return x;
};

a = printer_1(100);
console.log(a.typeof);
console.log(a);
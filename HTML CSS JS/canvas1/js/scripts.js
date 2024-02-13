function changeColor()
{
    var canvas1 = document.getElementById('canvas1');
    var canvas2 = document.getElementById('canvas2');

    var tempClassName = canvas1.className;
    canvas1.className = canvas2.className;
    canvas2.className = tempClassName;
}

function doRed()
{
    var canvas = document.getElementById('canvas1');
    var context = canvas.getContext('2d');

    context.clearRect(0, 0, canvas.width, canvas.height);
    canvas.style.backgroundColor = 'red';
}

function doBlue()
{
    var canvas = document.getElementById('canvas1');
    var context = canvas.getContext('2d');

    context.clearRect(0, 0, canvas.width, canvas.height);
    canvas.style.backgroundColor = 'blue';
}

function draw()
{
    var canvas = document.getElementById('canvas1');
    var context = canvas.getContext('2d');

    context.fillStyle = "yellow";
    context.fillRect(10, 10, 60, 60);
    context.fillRect(80, 10, 60, 60);

    context.fillStyle = "black";
    context.font = "20px Arial";
    context.fillText("Hello", 15, 45);
}
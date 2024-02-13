var canvas;
var context;
var color;
var radius;
var isPainting;

function init()
{
    canvas = document.getElementById('paintingArea');
    context = canvas.getContext('2d');
    isPainting = false;
    color = document.getElementById('colorSelector').value;
    radius = document.getElementById('brushSize').value;
}

function setWidth(value)
{
    if (isNaN(value))
    {
        value = '300';
        document.getElementById('widthText').value = value;
    }
    
    canvas.width = value;
}


function setHeight(value)
{
    if (isNaN(value))
    {
        value = '150';
        document.getElementById('heightText').value = value;
    }

    canvas.height = value;
}

function clearCanvas()
{
    context.clearRect(0, 0, canvas.width, canvas.height);
}

function startPainting()
{
    isPainting = true;
}

function endPainting()
{
    isPainting = false;
}

function doPaint(x, y)
{
    console.log(x, y);
    if (!isPainting)
    {
        return;
    }

    paintCircle(x, y);
}

function paintCircle (x, y)
{
    context.beginPath();
    
    context.arc(x, y, radius, 0, Math.PI * 2, true);
    context.fillStyle = color;
    context.fill();
}

function changeBrushSize()
{
    radius = document.getElementById('brushSize').value;
    document.getElementById('brushSizeLabel').innerHTML = radius;
}

function changeBrushColor()
{
    color = document.getElementById('colorSelector').value;
}
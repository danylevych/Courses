function changeColor()
{
    var canvas = document.getElementById('canvas1');
    var context = canvas.getContext('2d');

    context.clearRect(0, 0, canvas.width, canvas.height);
    canvas.style.backgroundColor = document.getElementById('colorSelector').value;
}

function drawSquare()
{
    changeColor();
    var canvas = document.getElementById('canvas1');
    var context = canvas.getContext('2d');
    var suqareMeasure = document.getElementById("squareMeasure").value;

    context.fillStyle = "yellow";
    context.fillRect(10, 10, suqareMeasure, suqareMeasure);

    context.fillStyle = "red";
    context.fillRect(20 +  parseInt(suqareMeasure), 10, suqareMeasure, suqareMeasure);
}
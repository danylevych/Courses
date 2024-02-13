var originalImage = null;

var nameOfColors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
var rainbowColors = {
    "red"    : {"r": 255, "g": 0,   "b": 0},
    "orange" : {"r": 255, "g": 165, "b": 0},
    "yellow" : {"r": 255, "g": 255, "b": 0},
    "green"  : {"r": 0,   "g": 255, "b": 0},
    "blue"   : {"r": 0,   "g": 0,   "b": 255},
    "indigo" : {"r": 75,  "g": 0,   "b": 130},
    "violet" : {"r": 143, "g": 0,   "b": 155},
}

function isImage()
{
    if (originalImage == null) 
    {
        alert("The image was not loaded.");
        return false;
    }
    return true;
}

function displayImage(image)
{
    var canvas = document.getElementById('imageArea');
    image.drawTo(canvas);
}

function getAvarage(pixel)
{
    return (pixel.getRed() + pixel.getGreen() + pixel.getBlue()) / 3;
}


function loadImage()
{
    var fileInput = document.getElementById('fileInput');
    originalImage = new SimpleImage(fileInput);
    displayImage(originalImage);
}

function doRed() 
{
    if (!isImage())
    {
        return;
    }

    var redImage = new SimpleImage(originalImage.width, originalImage.height);

    for (var pixel of redImage.values()) {
        var x = pixel.getX();
        var y = pixel.getY();
        
        var originalPixel = originalImage.getPixel(x, y);
        
        pixel.setRed(255);
        pixel.setGreen(originalPixel.getGreen());
        pixel.setBlue(originalPixel.getBlue());
    }

    displayImage(redImage);
}

function doGray()
{
    if (!isImage())
    {
        return;
    }

    var grayImage = new SimpleImage(originalImage.width, originalImage.height);

    for (var pixel of grayImage.values())
    {
        var avgValue = getAvarage(originalImage.getPixel(pixel.getX(), pixel.getY()));
        
        pixel.setRed(avgValue);
        pixel.setGreen(avgValue);
        pixel.setBlue(avgValue);
    }

    displayImage(grayImage);
}

function doWave()
{
    if (!isImage())
    {
        return;
    }

    var width = originalImage.width;
    var height = originalImage.height;
    var waveImage = new SimpleImage(width, height);
    
    var culculateUpperBorder = function(x) {
        return Math.cos(0.1 * x) * 20 + 20;
    }

    var culculateLowerBorder = function(x) {
        return Math.sin(0.1 * x) * 20 + height - 20;
    }

    for (var pixel of waveImage.values())
    {
        var x = pixel.getX();
        var y = pixel.getY();
        
        var upperBorder = culculateUpperBorder(x);
        var lowerBorder = culculateLowerBorder(x);

        // If our y cord is less then upper bound or more then lower bound 
        // left the default - black pixel.
        if ((y >= 0 && y <= upperBorder) || (y <= height && y >= lowerBorder))
        {
            continue;
        }
        
        waveImage.setPixel(x, y, originalImage.getPixel(x, y));
    }

    displayImage(waveImage);
}

function doRainbow()
{
    if (!isImage())
    {
        return;
    }

    var width = originalImage.width;
    var height = originalImage.height;
    var oneColorDistance = height / nameOfColors.length;

    var rainbowImage = new SimpleImage(width, height);

    // Return the value for some color for pixel.
    var getAvgColor = function(color, avg) {
        if (avg < 128) {
            return (color / 127.5) * avg;
        }
        else {
            return (2 - color / 127.5) * avg + 2 * color - 255
        }
    }

    for (var pixel of rainbowImage.values())
    {
        var x = pixel.getX();
        var y = pixel.getY();

        // Get a correct color.
        var index = Math.round(y / oneColorDistance) % nameOfColors.length;

        var colorName = nameOfColors[index];

        // Get an avarage value.
        var avgColor = getAvarage(originalImage.getPixel(x, y));
        
        // Set colors.
        pixel.setRed(getAvgColor(rainbowColors[colorName]["r"], avgColor));
        pixel.setGreen(getAvgColor(rainbowColors[colorName]["g"], avgColor));
        pixel.setBlue(getAvgColor(rainbowColors[colorName]["b"], avgColor));
    }

    displayImage(rainbowImage);
}

function doBlur() 
{
    if (!isImage())
    {
        return;
    }

    var width = originalImage.width;
    var height = originalImage.height;
    var blurImage = new SimpleImage(width, height);

    var getRandomCordinate = function(cord, offset, lower, upper) {
        var newCord = null;
        while (newCord == null || newCord < lower || newCord > upper) {
            // Generate the value in the range from cord - offset to cord + offset.
            newCord = Math.random() * ((cord + offset) - (cord - offset)) + (cord - offset);
        }
        return newCord;
    }

    for (var pixel of blurImage.values())
    {
        var x = pixel.getX();
        var y = pixel.getY();

        // We generate a value, and then check if it is less then 0.5
        // if the condition is true we aplay 'blure' for the pixel.
        if (Math.random() < 0.5)
        {
            // Find the new values for x and y.
            var newX = getRandomCordinate(x, 5, 0, width - 1);
            var newY = getRandomCordinate(y, 5, 0, height - 1);

            blurImage.setPixel(x, y, originalImage.getPixel(newX, newY));
        }
        else
        {
            blurImage.setPixel(x, y, originalImage.getPixel(x, y));
        }
    }

    displayImage(blurImage);
}

function resetFilter() 
{
    if (isImage()) 
    {
        displayImage(originalImage);
    }
}
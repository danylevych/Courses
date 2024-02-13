var bgImage = null;
var fgImage = null;


function uploadForeground()
{
    upload('uploadButtonForeground', fgImage, 'foregroundImageArea');
}

function uploadBackground()
{
    upload('uploadButtonBackground', bgImage, 'backgroundImageArea');
}

function upload(fromId, whereObj, whereCnvasId)
{
    var canvas = document.getElementById(whereCnvasId);
    var fileInput = document.getElementById(fromId);
    whereObj = new SimpleImage(fileInput);
    whereObj.drawTo(canvas);
}

function combineImage() 
{
    if (fgImage == null || !fgImage.complete())
    {
        alert("Error with the foreground image");
        return;
    }

    if (bgImage == null || !bgImage.complete())
    {
        alert("Error with the backround image");
        return;
    }
    
    // Clear all canvases after combining;
    clearCanvases();

    var combineImg = new SimpleImage(fgImage.width, fgImage.height);

    for (var pixel of fgImage.values())
    {
        var x = pixel.getX();
        var y = pixel.getY();

        if (pixel.getGreen() > pixel.getRed() + pixel.getBlue())
        {
            combineImg.setPixel(x, y, bgImage.getPixel(x, y));
        }
        else
        {
            combineImg.setPixel(x, y, pixel);
        }
    }



    // Show the combined img.    
    combineImg.drawTo(document.getElementById('foregroundImageArea'));
}


function clearCanvases()
{
    var backCanvas = document.getElementById('backgroundImageArea');
    var foreCanvas = document.getElementById('foregroundImageArea');

    var bgContext = backCanvas.getContext('2d');
    var fgContext = foreCanvas.getContext('2d');

    fgContext.clearRect(0, 0, foreCanvas.width, foreCanvas.height);
    bgContext.clearRect(0, 0, backCanvas.width, backCanvas.height);
}

// This is for another task.
// function makeGray()
// {
//     //var fileInput = document.getElementById('uploadButton');
//     //var image = new SimpleImage(fileInput);

//     for (var pixel of modefidedImage.values())
//     {
//         var avgValue = getAvg(pixel);
//         pixel.setRed(avgValue);
//         pixel.setGreen(avgValue);
//         pixel.setBlue(avgValue);
//     }

//     var canvas = document.getElementById('modifiedImageArea');
//     modefidedImage.drawTo(canvas);
// }

// function getAvg(pixel)
// {
//     return (pixel.getRed() + pixel.getGreen() + pixel.getBlue()) / 3;
// }
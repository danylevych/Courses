function changeColor()
{
    var div1 = document.getElementById("div1");
    var div2 = document.getElementById("div2");

    div1.className = "darkColor";
    div2.className = "brightColor";
}

function changeText()
{
    var div1 = document.getElementById("div1");
    var div2 = document.getElementById("div2");
    
    div1.innerHTML = "Hello";
    div1.style.color = "black";
    div2.innerHTML = "Bay";
}
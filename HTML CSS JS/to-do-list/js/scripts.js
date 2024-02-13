function addTask () 
{
    var input = document.getElementById("input");
    // get current text from input field

    var newTask = input.value;
    // only add new item to list if some text was entered
    if (newTask != "")
    {
      // create new HTML list item
        var item = document.createElement("li");
      // add HTML for buttons and new task text
      // Note, need to use '' because of "" in HTML
        item.innerHTML = '<input type="button" class="done" onclick="markDone(this.parentNode)" value="&#x2713;" /> ' + 
        '<input type="button" class="remove" onclick="remove(this.parentNode)" value="&#x2715;" />' + 
        '<input type="button" class="important" onclick="important(this.parentNode)" value="!" />' + '<span>' +
        newTask + "</span>";
      // add new item as part of existing list
        document.getElementById("tasks").appendChild(item);  

        input.value = "";
    }
}
  // change styling used for given item
function markDone (item) 
{ 
    if (item.className == '')
    {
        item.className = 'finished';
    }
    else
    {
        item.className = '';
    }
}

/* Step 7 below here */
function remove (item) {
    if (item.className == 'finished')
    {
        item.remove();
    }
}

  /* Step 11 below here */
function doAbout() {
    var aboutText = document.getElementById('divAbout');

    if (aboutText.style.display == 'none')
    {
        aboutText.style.display = 'block';
    }
    else
    {
        aboutText.style.display = 'none';
    }
}

var previousClassName = 'importantTask';
function important(item)
{
    var tempClassName = item.className;
    item.className = previousClassName;
    previousClassName = tempClassName;
}
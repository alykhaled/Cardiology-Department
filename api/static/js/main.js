var dashIcon = document.getElementById("dashIcon");
var operationsIcon = document.getElementById("operationsIcon");
var patientsIcon = document.getElementById("patientsIcon");
var nursesIcon = document.getElementById("nursesIcon");
var roomsIcon = document.getElementById("roomsIcon");
var menuBtn = document.getElementById("menuBtn");
var mainContent = document.getElementById("mainContent");
roomsIcon.classList.add('selected');

var isMenuOpen = false;
function openMenu(e)
{
    if(isMenuOpen)
    {
        isMenuOpen = false;
        myNavbar.classList.remove('open');        
    }
    else
    {
        isMenuOpen = true;
        myNavbar.classList.add('open');  
        console.log("test")      
    }
}

function chooseView(e)
{
    var ul = document.getElementById("navBar");
    var items = ul.getElementsByTagName("li");
    for (var i = 0; i < items.length; ++i) {
        console.log(items[i].classList);
        items[i].classList.remove('selected');
        console.log(items[i].classList);
    }
    e.classList.add('selected');
}
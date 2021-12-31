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
var isShown = false;
function classToggle() {
    const navs = document.querySelectorAll('.Navbar__Items');
    const bottom_links = document.querySelectorAll('.bottom-link');
    const navBar = document.getElementById("bottom-navbar");
    console.log(isShown);
    navs.forEach(nav => nav.classList.toggle('Navbar__ToggleShow'));
    bottom_links.forEach(bottom_links => bottom_links.classList.toggle('bottom-link-move-up'));
    navBar.classList.toggle('Navbar__ToggleShow');
    if (isShown) {
        moveDown();
    }
    else
    {
        moveUp();
    }
  }
  
function moveUp() {
    document.querySelector('.Navbar__Link-toggle').style.bottom = "20%";
    document.querySelector('.Navbar__Link-toggle').innerHTML = "x";
    
    isShown = true;
}

function moveDown() {
    document.querySelector('.Navbar__Link-toggle').style.bottom = "10%";
    document.querySelector('.Navbar__Link-toggle').innerHTML = "+";
    isShown = false;
}

document.querySelector('.Navbar__Link-toggle').addEventListener('click', classToggle);

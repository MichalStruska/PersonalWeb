var isShown = false;
function classToggle() {
    // if (isShown) {
    //     moveDown();
    // }
    // else
    // {
    //     moveUp();
    // }
    
    const bottom_links = document.querySelectorAll('.bottom-link');
    const navBar = document.getElementById("bottom-navbar");

    bottom_links.forEach(bottom_links => bottom_links.classList.toggle('bottom-link-move-up'));
    navBar.classList.toggle('active');
    document.getElementById("content-container").classList.toggle('content-container-up');

  }
  
function moveUp() {
    if ((IsPhone()) && (IsLandscape()))
    {
        document.querySelector('.navbar-toggle').style.bottom = "42%";
    }
    else
    {
        document.querySelector('.navbar-toggle').style.bottom = "25%";
    }
    document.querySelector('.navbar-toggle').innerHTML = "x";
    
    isShown = true;
}

function IsLandscape() {
    return (screen.availHeight < screen.availWidth);
}

function IsPhone()
{
    return (/Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test(navigator.userAgent));
}

function moveDown() {
    document.querySelector('.navbar-toggle').style.bottom = "5%";
    document.querySelector('.navbar-toggle').innerHTML = "+";
    isShown = false;
}

document.querySelector('.navbar-toggle').addEventListener('click', classToggle);

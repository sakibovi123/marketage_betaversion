// ========================================================================
                            // For  Nav bar menu
// ========================================================================

let hamburgerMenu = document.querySelector(".hamburger__menu");
let mobileNavLinks = document.querySelector(".mobile__navLinks");
let closeBtn = document.querySelector(".nav__close");
let bodyTag = document.querySelector("body");


let overlay = document.querySelector(".overlay");
let backGround = document.querySelector(".bg__fixed");

hamburgerMenu.addEventListener('click', () => {
    mobileNavLinks.classList.add("active__navLinks");
    overlay.style.display = 'block';
    bodyTag.style.overflow = 'hidden';
    backGround.style.display = 'block';

});

closeBtn.addEventListener("click", () => {
    mobileNavLinks.classList.remove("active__navLinks");
    overlay.style.display = 'none';
    bodyTag.style.overflow = 'visible';
    backGround.style.display = 'none';

});
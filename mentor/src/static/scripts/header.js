const header_btn = document.getElementById("header-menu-btn");
const header_alt_nav = document.getElementById("header-alt-nav");

const toggleMenu = function () {
    if (!header_alt_nav.classList.contains("visible")) {
        header_alt_nav.classList.add("visible")
    }else {
        header_alt_nav.classList.remove("visible")
    }
}

header_btn.addEventListener("click", toggleMenu)
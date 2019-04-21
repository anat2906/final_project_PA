(function toTopBtn() {
  var button = document.createElement("button");
  button.classList.add("btn", "btn-primary", "toTop");
  document.body.appendChild(button);
  document.body.setAttribute("style", "scroll-behavior: smooth");
  document.documentElement.setAttribute("style", "scroll-behavior: smooth");

  button.addEventListener("click", toTopFunc);

  window.addEventListener("scroll", scrollFunc);

  function toTopFunc() {
    document.body.scrollTop = 0;
    document.documentElement.scrollTop = 0;
  }

  function scrollFunc() {
    if (
      document.body.scrollTop > 500 ||
      document.documentElement.scrollTop > 500
    ) {
      button.style.display = "block";
    } else {
      button.style.display = "none";
    }
  }
})();

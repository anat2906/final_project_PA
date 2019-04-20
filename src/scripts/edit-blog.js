(function() {
  const body = document.body;
  const new_body = body.innerHTML
    .replace("Currently:", "")
    .replace("Change:", "");
  body.innerHTML = new_body;
})();

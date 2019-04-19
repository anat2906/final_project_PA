var modalLogin = document.getElementById("modal-login");
var loginBtn = document.getElementById("btn-login");
var modalLoginClose = document.getElementsByClassName("modal-login__close")[0];
var modalJoin = document.getElementById("modal-join-mentee");
var joinBtn = document.getElementById("btn-join");
var modalJoinClose = document.getElementsByClassName("modal-join__close")[1];

loginBtn.addEventListener("click", () => {
    modalLogin.style.display = "block"
})

modalLoginClose.addEventListener("click", () => {
    modalLogin.style.display = "none"
})

joinBtn.addEventListener("click", () => {
    modalJoin.style.display = "block"
})

joinBtn.addEventListener("click", () => {
    modalJoin.style.display = "block"
    console.log("BTN!")
})
modalJoinClose.addEventListener("click", () => {
    modalJoin.style.display = "none"
})


(function() {
  var doc = document;
  index = 1;
  var Slider = function() {
    this.box = doc.querySelector(".mainpage__reviews-block__carousel");
    this.slidesBox = doc.querySelector(
      ".mainpage__reviews-block__review-div__carousel-slides"
    );
    this.slides = doc.querySelectorAll(
      ".mainpage__reviews-block__review-div__carousel-item"
    );

    this.btns = doc.querySelectorAll(".mainpage__reviews-block__btn");
    this.size = this.box.clientWidth;

    this.position();
    this.carousel();
  };
  Slider.prototype.position = function() {
    var size = this.size;
    this.slidesBox.style.transform = "translateX(" + -index * size + "px)";
  };

  Slider.prototype.carousel = function() {
    var i,
      max = this.btns.length,
      that = this;

    for (i = 0; i < max; i += 1) {
      that.btns[i].addEventListener(
        "click",
        Slider[that.btns[i].id].bind(null, that)
      );
    }
  };

  Slider.prevbtn = function(box) {
    box.slidesBox.style.transition = "transform .3s ease-in-out";
    var size = box.size;
    index <= 0 ? false : index--;
    box.slidesBox.style.transform = "translateX(" + -index * size + "px)";
    box.jump();
  };

  Slider.nextbtn = function(box) {
    box.slidesBox.style.transition = "transform .3s ease-in-out";
    var max = box.slides.length;
    var size = box.size;
    index >= max - 1 ? false : index++;
    box.slidesBox.style.transform = "translateX(" + -index * size + "px)";
    box.jump();
  };

  Slider.prototype.jump = function() {
    var that = this;
    var size = this.size;
    this.slidesBox.addEventListener("transitionend", function() {
      that.slides[index].id === "firstClone" ? (index = 1) : index;
      that.slides[index].id === "lastClone"
        ? (index = that.slides.length - 2)
        : index;
      that.slidesBox.style.transition = "none";
      that.slidesBox.style.transform = "translateX(" + -index * size + "px)";
    });
  };

  new Slider();
})();

(function() {
  document.querySelector(".mainpage__third-block__cards-carousel").slick({
    infinite: true,
    slidesToShow: 3,
    slidesToScroll: 3
  });
})();

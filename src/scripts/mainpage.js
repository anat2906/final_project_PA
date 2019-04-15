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
    console.log(this.size)
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

  Slider.prevbtn = function Pre(box) {
    box.slidesBox.style.transition = "transform .3s ease-in-out";
    var size = box.size;
    index <= 0 ? false : index--;
    box.slidesBox.style.transform = "translateX(" + -index * size +20 + "px)";
    box.jump();
  };

  Slider.nextbtn = function Next(box) {
    box.slidesBox.style.transition = "transform .3s ease-in-out";
    var max = box.slides.length;
    var size = box.size;
    index >= max - 1 ? false : index++;
    box.slidesBox.style.transform = "translateX(" + -index * size + 20 + "px)";
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

(function(){
  var words = document.getElementsByClassName('word');
  var wordArray = [];
  var currentWord = 0;

  words[currentWord].style.opacity = 1;
  for (var i = 0; i < words.length; i++) {
    splitLetters(words[i]);
  }

  function changeWord() {
    var cw = wordArray[currentWord];
    var nw = currentWord == words.length-1 ? wordArray[0] : wordArray[currentWord+1];
    for (var i = 0; i < cw.length; i++) {
      animateLetterOut(cw, i);
    }
    
    for (var i = 0; i < nw.length; i++) {
      nw[i].className = 'letter behind';
      nw[0].parentElement.style.opacity = 1;
      animateLetterIn(nw, i);
    }
    
    currentWord = (currentWord == wordArray.length-1) ? 0 : currentWord+1;
  }

  function animateLetterOut(cw, i) {
    setTimeout(function() {
      cw[i].className = 'letter out';
    }, i*80);
  }

  function animateLetterIn(nw, i) {
    setTimeout(function() {
      nw[i].className = 'letter in';
    }, 340+(i*80));
  }

  function splitLetters(word) {
    var content = word.innerHTML;
    word.innerHTML = '';
    var letters = [];
    for (var i = 0; i < content.length; i++) {
      var letter = document.createElement('span');
      letter.className = 'letter';
      letter.innerHTML = content.charAt(i);
      word.appendChild(letter);
      letters.push(letter);
    }
    
    wordArray.push(letters);
  }

  changeWord();
  setInterval(changeWord, 4000);
})()

// (function() {
//   document.querySelector(".mainpage__third-block__cards-carousel").slick({
//     infinite: true,
//     slidesToShow: 3,
//     slidesToScroll: 3
//   });
// })();

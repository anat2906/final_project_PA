(function() {
  (function() {
    var doc = document;
    var slides = doc.querySelectorAll(
      ".mainpage__reviews-block__review-div__carousel-item"
    );
    var btnPrev = doc.querySelector("#prevbtn");
    var btnNext = doc.querySelector("#nextbtn");
    var current = 0;
    //
    function nextSlide() {
      for (let i = 0; i < slides.length; i++) {
        slides[i].classList.add("opacity0");
      }
      slides[current].classList.remove("opacity0");
    }
    function slider() {
      if (current + 1 == slides.length) {
        current = 0;
      } else {
        current++;
      }
      nextSlide();
    }
    //
    btnNext.addEventListener("click", function() {
      slider();
    });
    //
    btnPrev.addEventListener("click", function() {
      if (current - 1 == -1) {
        current = slides.length - 1;
      } else {
        current--;
      }
      nextSlide();
    });
    //

    setInterval(slider, 3500);
  })();

  //
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
  //
  (function slickCarousel() {
    $(".mainpage__third-block__cards-carousel").slick({
      speed: 200,
      arrows: false,
      dots: true,
      slidesToShow: 3,
      adaptiveHeight: true,
      initialSlide: -1,
      autoplay: true,
      autoplaySpeed: 1500,
      responsive: [
        {
          breakpoint: 1024,
          settings: {
            slidesToShow: 2,
            slidesToScroll: 1,
            infinite: true,
            dots: true
          }
        },
        {
          breakpoint: 600,
          settings: {
            slidesToShow: 1,
            slidesToScroll: 1
          }
        },
        {
          breakpoint: 480,
          settings: {
            unslick: true,
            slidesToShow: 1,
            slidesToScroll: 1
          }
        }
      ]
    });
  })();
  //
  (function() {
    var words = document.getElementsByClassName("word");
    var wordArray = [];
    var currentWord = 0;

    words[currentWord].style.opacity = 1;
    for (var i = 0; i < words.length; i++) {
      splitLetters(words[i]);
    }

    function changeWord() {
      var cw = wordArray[currentWord];
      var nw =
        currentWord == words.length - 1
          ? wordArray[0]
          : wordArray[currentWord + 1];
      for (var i = 0; i < cw.length; i++) {
        animateLetterOut(cw, i);
      }

      for (var i = 0; i < nw.length; i++) {
        nw[i].className = "letter behind";
        nw[0].parentElement.style.opacity = 1;
        animateLetterIn(nw, i);
      }

      currentWord = currentWord == wordArray.length - 1 ? 0 : currentWord + 1;
    }

    function animateLetterOut(cw, i) {
      setTimeout(function() {
        cw[i].className = "letter out";
      }, i * 80);
    }

    function animateLetterIn(nw, i) {
      setTimeout(function() {
        nw[i].className = "letter in";
      }, 340 + i * 80);
    }

    function splitLetters(word) {
      var content = word.innerHTML;
      word.innerHTML = "";
      var letters = [];
      for (var i = 0; i < content.length; i++) {
        var letter = document.createElement("span");
        letter.className = "letter";
        letter.innerHTML = content.charAt(i);
        word.appendChild(letter);
        letters.push(letter);
      }

      wordArray.push(letters);
    }

    changeWord();
    setInterval(changeWord, 3000);
  })();
})();

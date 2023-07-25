
$(document).ready(function() {
    var slides = $('#hero-slider .slide');
    var currentSlide = 0;
  
    function showSlide(index) {
      slides.removeClass('active');
      slides.eq(index).addClass('active');
    }
  
    function nextSlide() {
      currentSlide = (currentSlide + 1) % slides.length;
      showSlide(currentSlide);
    }
  
    // Start the slider
    showSlide(currentSlide);
    setInterval(nextSlide, 5000);

    // document.getElementById("cat-tray").style.width = document.getElementsByClassName("header-category")[0].style.width;
});

$(document).ready(function() {
    var slider = $('.slider');
    var slideWidth = $('.product').outerWidth();
    var slideCount = $('.product').length;
    var totalWidth = slideWidth * slideCount;
    var visibleSlides = Math.floor($('.prod-container').width() / slideWidth);
    var currentSlide = 0;
  
    $('.slider').css('width', totalWidth);
  
    function slideNext() {
      currentSlide++;
      if (currentSlide > slideCount - visibleSlides) {
        currentSlide = 0;
      }
      slider.css('transform', 'translateX(' + ((-slideWidth * currentSlide) - (currentSlide * 32) ) + 'px)');
    }
  
    function slidePrev() {
      currentSlide--;
      if (currentSlide < 0) {
        currentSlide = slideCount - visibleSlides;
      }
      slider.css('transform', 'translateX(' + (-slideWidth * currentSlide) + 'px)');
    }
  
    $('.next-btn').on('click', slideNext);
    $('.prev-btn').on('click', slidePrev);
  });
  

function URL_dispatcher(id) {
    console.log(```products/${String(id)}```);
    location.href = ```products/${String(id)}```;
  }



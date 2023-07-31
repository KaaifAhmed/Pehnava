
$(document).ready(function() {
    localStorage.clear()
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
  function initializeSlider(slider) {
    var sliderContainer = slider.find('.slider');
    var slides = sliderContainer.find('.product');
    var slideWidth = slides.outerWidth();
    var slideCount = slides.length;
    var totalWidth = slideWidth * slideCount;
    var visibleSlides = Math.floor(sliderContainer.width() / slideWidth);
    var currentSlide = 0;
  
    sliderContainer.css('width', totalWidth);
  
    function slideNext() {
      currentSlide++;
      if (currentSlide > slideCount - visibleSlides) {
        currentSlide = 0;
      }
      sliderContainer.css('transform', 'translateX(' + (-slideWidth * currentSlide) + 'px)');
    }
  
    function slidePrev() {
      currentSlide--;
      if (currentSlide < 0) {
        currentSlide = slideCount - visibleSlides;
      }
      sliderContainer.css('transform', 'translateX(' + (-slideWidth * currentSlide) + 'px)');
    }
  
    slider.find('.next-btn').on('click', slideNext);
    slider.find('.prev-btn').on('click', slidePrev);
  }

  // Call the function to initialize all sliders
  $('.prod-container').each(function() {
    initializeSlider($(this));
  });
});

  

function URL_dispatcher(id) {
    console.log(```products/${String(id)}```);
    location.href = ```products/${String(id)}```;
  }

 




function button () {
  document.querySelector('.order-success').style.display='none';
  location.href = "/";
}
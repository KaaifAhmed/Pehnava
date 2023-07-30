
document.addEventListener('DOMContentLoaded', function() {
    let mainImage = document.getElementById('main-img');
    let smallImages = document.querySelectorAll('.small-image');

    let main_img = document.getElementById('main-img');
    let container = document.getElementById('small-images-container');

    document.getElementById("product-sizes").firstElementChild.classList.add("selected-size")
    
    try {
      let lens = document.getElementById('lens');
      lens.style.left = container.offsetWidth + 25 + 'px';
      lens.style.height = main_img.offsetHeight + 'px';
    } catch (error) {
    }

  
    smallImages.forEach(function(image) {
        image.addEventListener('click', function() {
            var newImageSrc = this.src;
            mainImage.src = newImageSrc;
        });
    });
    
    let prodDesc = document.querySelectorAll('.details-head');
    prodDesc.forEach(function (head) {
        head.addEventListener('click', function(){
            document.querySelector('.current-detail').classList.remove('current-detail');
            head.classList.add('current-detail');
        })
    })

    let prodDetails = document.getElementById('details--1');
    const details = prodDetails.innerHTML;
    let detBtn = document.getElementById('prod-det');
    let shipBtn = document.getElementById('prod-det-ship');
    let careBtn = document.getElementById('prod-det-care');

    detBtn.addEventListener('click', function() {
      prodDetails.innerHTML = details;
    })

    shipBtn.addEventListener('click', function() {
      prodDetails.innerHTML = `<ul style="margin-bottom: 10px; display: flex; flex-direction: column; gap: 8px; list-style: none;">
      <li>
      Items returned without authorization will not be accepted.</li>
      <li>
      Items must be returned within 30 days after you receive them.</li>
      <li>
      All items must be in the same condition that you received it, unworn or unused, with tags, and in its original packaging. You will also need the receipt or proof of purchase.</li>
      <li>When returning or exchanging items, customers must use a shipping method providing tracking information.</li>
  </ul>`;
    })

    careBtn.addEventListener('click', function() {
      prodDetails.innerHTML = `<ul style="margin-bottom: 10px; display: flex; flex-direction: column; gap: 8px; list-style: none;">
      <li>Wash your clothes less.</li>
      <li>Wash everything on delicate or hand wash.</li>
      <li>Wash everything on cold.</li>
      <li>Hang dry delicate items.</li>
      <li>Store your clothes properly.</li>
  </ul>`;
    })

    
  });
function sizeChart(cmd) {
  if (cmd === "open") {
    document.getElementById('size-chart').style.display = 'flex';
  } else {
    document.getElementById('size-chart').style.display = 'none';
  }
}

function sizeSelect(id) {
  document.querySelector('.selected-size').classList.remove('selected-size');
  document.getElementById(id).classList.add('selected-size');
}


var addBtn = document.getElementById('qty-add');
var subtractBtn = document.getElementById('qty-sub');
var total = parseInt(document.getElementById('pr-qty').innerText);
if (total == 0) {
  var number = 0;
  document.getElementById('prod-qty').innerText = 0;
} else {
  var number = 1;
  document.addEventListener('DOMContentLoaded', function() {
      var numberElement = document.getElementById('prod-qty');  
      addBtn.addEventListener('click', function() {
        if (number < total) {
          number++;
          numberElement.textContent = number;
          if (! addBtn.classList.contains('animatedButton')) {
            addBtn.classList.add('animatedButton');
            addBtn.style.opacity = 1;
          }
          if (number == total) {
            addBtn.classList.remove('animatedButton');
            addBtn.style.opacity = 0.3;
          }
          if (number != 1) {
            subtractBtn.classList.add('animatedButton');
            subtractBtn.style.opacity = 1;
          }
        } else {
          addBtn.classList.remove('animatedButton');
          addBtn.style.opacity = 0.3;
        }
      });
    
      subtractBtn.addEventListener('click', function() {
        if (number > 1) {
          number--;
          numberElement.textContent = number;
          if (! subtractBtn.classList.contains('animatedButton')) {
            subtractBtn.classList.add('animatedButton');
            subtractBtn.style.opacity = 1;
          }
          if (number != total) {
            addBtn.classList.add('animatedButton');
            addBtn.style.opacity = 1;
          }
          if (number == 1) {
            subtractBtn.classList.remove('animatedButton');
            subtractBtn.style.opacity = 0.3;
          }
        } else {
          subtractBtn.classList.remove('animatedButton');
          subtractBtn.style.opacity = 0.3;
        }
      });

  });
  }


    
if (number == 1) {
  subtractBtn.classList.remove('animatedButton');
  subtractBtn.style.opacity = 0.3;
} if (number == 1 && total == 1) {
  addBtn.classList.remove('animatedButton');
  addBtn.style.opacity = 0.3;
} if (number == 0 && total == 0) {
  subtractBtn.classList.remove('animatedButton');
  subtractBtn.style.opacity = 0.3;
  addBtn.classList.remove('animatedButton');
  addBtn.style.opacity = 0.3;
}


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




function isMobileDevice() {
  return /Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test(navigator.userAgent);
}

function ImageZoom(imgId) {
  
  if (!isMobileDevice()) {
    let img = document.getElementById(imgId)
    let lens = document.getElementById('lens')
    var pos = 0;
    
  
    
    let ratio = 3;
    lens.style.backgroundSize = `${img.width*ratio}px ${img.height*ratio}px`;
    
    
  
  lens.addEventListener("mouseout", function name(event) {
    
    lens.style.backgroundImage = 'none'
    
  })
  lens.addEventListener("mouseover", function name(event) {
    lens.style.backgroundImage = `url(${img.src})`;
  })  
    lens.addEventListener("mousemove", function movelens(event) {
      
      let pos = getCursor(event);
      error_rate = 30 ;
          if (pos.x >= 320) {pos.x = 320};
          if (pos.y >= 479) {pos.y = 479};
          lens.style.backgroundPosition = `-${pos.x*ratio}px -${pos.y*ratio}px`              
              })  
           
} else {
  console.log("a mobile device");
  if (lens) {
    lens.remove();
    console.log("lens has removed");
  }
  console.log("nope", lens);
}
  
  function getCursor(event) {
    let img = document.getElementById("main-img")
    let bounds = img.getBoundingClientRect()
    
    let x = event.pageX - bounds.left;
    let y = event.pageY - bounds.top;
    return {'x':x, 'y':y}
  }
}

ImageZoom('main-img')


let slider = document.getElementsByClassName("slider")[0].children;
let suggested = document.getElementById("suggested")
let p = document.getElementById("product-slider-p");
let n = document.getElementById("product-slider-n");
// console.log(slider);
if (slider.length > 0) {
  suggested.innerText = "Suggested Products";
  p.style.display = 'block';
  n.style.display = 'block';
  
} else {
  suggested.innerText = "No Currently Suggested Products";
  p.style.display = 'none';
  n.style.display = 'none';
  

}
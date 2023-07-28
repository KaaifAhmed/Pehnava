
const container = document.getElementById("cat-tray");
  // where "container" is the id of the container
    container.addEventListener("wheel", function (e) {
      if (e.deltaY > 0) {
        container.scrollLeft += 150;
        e.preventDefault();
  // prevenDefault() will help avoid worrisome 
  // inclusion of vertical scroll 
      }
      else {
        container.scrollLeft -= 150;
        e.preventDefault();
}
});

// Function to detect overflow of #cat-tray element
function isOverflowing(element) {
  return element.scrollWidth > element.clientWidth;
}

// Get the #cat-tray element
const catTrayElement = document.getElementById('cat-tray');

// Check if it is overflowing
if (isOverflowing(catTrayElement)) {
  catTrayElement.style.justifyContent = "flex-start";
  // Do something here, like showing a scrollbar or hiding some content.
} else {
  catTrayElement.style.justifyContent = "center";
  // Do something else if it's not overflowing.
}
  
const cat_container = document.getElementById("cat-tray");
  let isDragging = false;
  let startScrollX, startX;

  cat_container.addEventListener("touchstart", (e) => {
    isDragging = true;
    startX = e.touches[0].clientX;
    startScrollX = container.scrollLeft;
  });

  cat_container.addEventListener("touchmove", (e) => {
    if (isDragging) {
      const moveX = e.touches[0].clientX;
      const distance = startX - moveX;
      container.scrollLeft = startScrollX + distance;
    }
  });

  cat_container.addEventListener("touchend", () => {
    isDragging=false;
});

let expandable = document.getElementById("expandable");

// $(document).ready(function () {
//   $(".header-category").css("display", "none");
//   console.log("hello");
// })

function catTrayToggle() {
  expandable.classList.toggle("tray-show")
  // expandable.style.opacity = expandable.style.opacity === '1' ? '0' : '1';
}
let slideIndex = 1;
showSlides(slideIndex);

// Next/previous controls
function plusSlides(n) {
  showSlides(slideIndex += n);
}

// Thumbnail image controls
function currentSlide(n) {
  showSlides(slideIndex = n);
}

function showSlides(n) {
  let i;
  let slides = document.getElementsByClassName("mySlides");
  let dots = document.getElementsByClassName("dot");
  if (n > slides.length) {slideIndex = 1}
  if (n < 1) {slideIndex = slides.length}
  for (i = 0; i < slides.length; i++) {
    slides[i].style.display = "none";
  }
  for (i = 0; i < dots.length; i++) {
    dots[i].className = dots[i].className.replace(" active", "");
  }
  slides[slideIndex-1].style.display = "block";
  dots[slideIndex-1].className += " active";
}

// Carrossel automático (opcional)
let autoSlideInterval = setInterval(() => {
    plusSlides(1);
}, 5000); // Muda a cada 5 segundos

// Pausa o carrossel quando o mouse está sobre ele
const slideshowContainer = document.querySelector('.slideshow-container');
slideshowContainer.addEventListener('mouseenter', () => {
    clearInterval(autoSlideInterval);
});

slideshowContainer.addEventListener('mouseleave', () => {
    autoSlideInterval = setInterval(() => {
        plusSlides(1);
    }, 5000);
});

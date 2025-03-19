// Your existing slide code, video triggers, and modals...
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



document.addEventListener("DOMContentLoaded", function() {
  // Adjust height for ratioDivs
  const divs = document.querySelectorAll('.ratioDiv');
  function adjustHeight() {
    const screenWidth = window.innerWidth;
    const targetHeight = (screenWidth * 1.5) / 4;
    divs.forEach(div => {
      div.style.height = `${targetHeight}px`;
    });
  }
  adjustHeight();
  window.addEventListener('resize', adjustHeight);
  
  // NAV TOGGLE FUNCTIONALITY FOR MOBILE
  const toggleButton = document.querySelector('.nav-toggle');
  const navLinks = document.querySelector('.nav-links');
  
  toggleButton.addEventListener('click', function() {
    navLinks.classList.toggle('active');
    toggleButton.classList.toggle('active'); // This rotates the arrow icon
  });
});

// Video trigger event listeners
document.querySelectorAll('.videoTrigger').forEach(trigger => {
  trigger.addEventListener('click', function() {
    const videoId = this.getAttribute('data-video-id');
    const popup = document.getElementById('videoPopup');
    const frame = document.getElementById('videoFrame');
    frame.src = `https://www.youtube.com/embed/${videoId}?autoplay=1`;
    popup.style.display = 'flex';
  });
});

// document.getElementById('videoPopup').addEventListener('click', function(event) {
//   if (event.target === this) {
//     closePopup();
//   }
// });

function closePopup() {
  const popup = document.getElementById('videoPopup');
  const frame = document.getElementById('videoFrame');
  popup.style.display = 'none';
  frame.src = "";
}

function openModal(src) {
  var modal = document.getElementById("fullscreenModal");
  var modalImg = document.getElementById("modalImage");
  modal.style.display = "flex";
  modalImg.src = src;
}

function closeModal() {
  var modal = document.getElementById("fullscreenModal");
  modal.style.display = "none";
}

function openVideoModal(videoId) {
  var modal = document.getElementById("videoModal");
  var iframe = document.getElementById("videoIframe");
  modal.style.display = "flex";
  iframe.src = `https://www.youtube.com/embed/${videoId}?autoplay=1`;
}

function closeVideoModal() {
  var modal = document.getElementById("videoModal");
  var iframe = document.getElementById("videoIframe");
  modal.style.display = "none";
  iframe.src = "";
}

function showSlides(n) {
  let i;
  let slides = document.getElementsByClassName("mySlides");
  let dots = document.getElementsByClassName("dot");
  if (slides.length === 0 || dots.length === 0) {
    return;
  }
  if (n > slides.length) { slideIndex = 1; }
  if (n < 1) { slideIndex = slides.length; }
  for (i = 0; i < slides.length; i++) {
    slides[i].style.display = "none";
  }
  for (i = 0; i < dots.length; i++) {
    dots[i].className = dots[i].className.replace(" active", "");
  }
  slides[slideIndex - 1].style.display = "block";
  dots[slideIndex - 1].className += " active";
}
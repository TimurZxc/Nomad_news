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

document.addEventListener("DOMContentLoaded", function() {
  const divs = document.querySelectorAll('.ratioDiv'); // Select all divs with the class 'ratioDiv'

  function adjustHeight() {
      const screenWidth = window.innerWidth;           // Get the current width of the screen
      const targetHeight = (screenWidth * 1.5) / 3.6;    // Calculate the height with the ratio 2:1.5

      divs.forEach(div => {
          div.style.height = `${targetHeight}px`;     // Set the new height for each div
      });
  }

  adjustHeight(); // Call once on initial load
  window.addEventListener('resize', adjustHeight);    // Adjust height on every window resize
});



document.querySelectorAll('.videoTrigger').forEach(trigger => {
  trigger.addEventListener('click', function() {
      const videoId = this.getAttribute('data-video-id');
      const popup = document.getElementById('videoPopup');
      const frame = document.getElementById('videoFrame');
      frame.src = `https://www.youtube.com/embed/${videoId}?autoplay=1`;
      popup.style.display = 'flex';
  });
});

document.getElementById('videoPopup').addEventListener('click', function(event) {
  if (event.target === this) {
      closePopup();
  }
});

function closePopup() {
  const popup = document.getElementById('videoPopup');
  const frame = document.getElementById('videoFrame');
  popup.style.display = 'none';
  frame.src = ""; // Stop video playback
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
  // If your videoUrl is a standard YouTube URL (e.g., watch?v=...), consider converting it to an embed URL.
  // For now, we assume the provided URL is already embeddable.
  iframe.src = `https://www.youtube.com/embed/${videoId}?autoplay=1`;
}



function closeVideoModal() {
  var modal = document.getElementById("videoModal");
  var iframe = document.getElementById("videoIframe");
  modal.style.display = "none";
  iframe.src = ""; // Reset the iframe to stop the video playback.
}
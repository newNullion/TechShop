document.addEventListener("DOMContentLoaded", function () {
  const track = document.querySelector(".carousel-track");
  const slides = document.querySelectorAll(".carousel-slide");

  const prevBtn = document.querySelector(".carousel-btn.prev");
  const nextBtn = document.querySelector(".carousel-btn.next");

  let index = 1;
  let isTransitioning = false;

  // Клонируем первый и последний слайд
  const firstClone = slides[0].cloneNode(true);
  const lastClone = slides[slides.length - 1].cloneNode(true);

  firstClone.classList.add("clone");
  lastClone.classList.add("clone");

  track.appendChild(firstClone);
  track.insertBefore(lastClone, slides[0]);

  const allSlides = document.querySelectorAll(".carousel-slide");
  const totalSlides = allSlides.length;

  const slideWidth = 100;

  track.style.transform = `translateX(-${index * slideWidth}%)`;

  function goToSlide(newIndex) {
    if (isTransitioning) return;
    isTransitioning = true;

    track.style.transition = "transform 0.5s ease-in-out";
    track.style.transform = `translateX(-${newIndex * slideWidth}%)`;
    index = newIndex;
  }

  track.addEventListener("transitionend", () => {
    isTransitioning = false;
    // Переход с клона на оригинал без анимации
    if (allSlides[index].classList.contains("clone")) {
      track.style.transition = "none";
      if (index === 0) {
        index = totalSlides - 2;
      } else if (index === totalSlides - 1) {
        index = 1;
      }
      track.style.transform = `translateX(-${index * slideWidth}%)`;
    }
  });

  nextBtn.addEventListener("click", () => {
    if (index >= totalSlides - 1) return;
    goToSlide(index + 1);
  });

  prevBtn.addEventListener("click", () => {
    if (index <= 0) return;
    goToSlide(index - 1);
  });
});



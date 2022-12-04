const swiper = new Swiper('.swiper', {
  slidesPerView: 7,
  loop: true,
  grab: true,
  navigation: {
    nextEl: '.swiper-button-next',
    prevEl: '.swiper-button-prev',
  },
  breakpoints: {
    220: {
      slidesPerView: 1,
      slideToClickedSlide: true,
    },
    320: {
      slidesPerView: 1,
      slideToClickedSlide: true,
    },
    480: {
      slidesPerView: 1,
    },
    640: {
      slidesPerView: 4,
    }
  }
});
document.addEventListener("DOMContentLoaded", function () {
  // Navbar scroll effect
  const navbar = document.getElementById('mainNavbar');
  const hero = document.querySelector('.hero');

  if (hero && navbar) {
    window.addEventListener('scroll', () => {
      const heroHeight = hero.offsetHeight;

      if (window.scrollY > heroHeight - 100) {
        navbar.classList.add('navbar-scrolled');
      } else {
        navbar.classList.remove('navbar-scrolled');
      }
    });
  }

  // Star rating rendering
  const ratingdivs = document.querySelectorAll(".rating");

  ratingdivs.forEach(ratingdiv => {
    const ratingvalue = parseFloat(ratingdiv.getAttribute("data-rating"));
    const stars = ratingdiv.querySelectorAll('i');

    for (let i = 0; i < Math.floor(ratingvalue); i++) {
      stars[i].classList.add("fa-solid", "fa-star");
    }

    if (ratingvalue % 1 >= 0.5 && stars[Math.floor(ratingvalue)]) {
      stars[Math.floor(ratingvalue)].classList.remove("fa-regular", "fa-star");
      stars[Math.floor(ratingvalue)].classList.add("fa-solid", "fa-star-half-stroke");
    }
  });
});

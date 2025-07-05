document.addEventListener('DOMContentLoaded', function () {
    const navbar = document.getElementById('mainNavbar');
    const hero = document.querySelector('.hero');

    if (!hero || !navbar) return;

    window.addEventListener('scroll', () => {
      const heroHeight = hero.offsetHeight;

      if (window.scrollY > heroHeight - 100) {
        navbar.classList.add('navbar-scrolled');
      } else {
        navbar.classList.remove('navbar-scrolled');
      }
    });
  });
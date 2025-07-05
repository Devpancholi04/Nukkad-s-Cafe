document.addEventListener("DOMContentLoaded", function () {
  
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

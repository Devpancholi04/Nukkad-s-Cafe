
document.addEventListener("DOMContentLoaded", function () {
  const categorySelect = document.getElementById("categories");
  const searchInput = document.querySelector("input[name='search']");
  const searchButton = document.querySelector(".btn-warning");
  const menuSections = document.querySelectorAll(".category-section");


  function filterMenu() {
    const selectedCategory = categorySelect.value.trim();
    const searchTerm = searchInput.value.trim().toLowerCase();


    const params = new URLSearchParams(window.location.search);
    if (selectedCategory && selectedCategory !== "Select the categories") {
      params.set("category", selectedCategory);
    } else {
      params.delete("category");
    }

    if (searchTerm) {
      params.set("search", searchTerm);
    } else {
      params.delete("search");
    }

    const newUrl = `${window.location.pathname}?${params.toString()}`;
    window.history.pushState({}, "", newUrl);


    menuSections.forEach(section => {
      const category = section.dataset.category.trim();
      let visibleItems = 0;

      section.querySelectorAll(".col-6").forEach(item => {
        const itemName = item.querySelector(".menu-name-price span")?.textContent.trim().toLowerCase() || "";

        const matchCategory =
          selectedCategory === "Select the categories" ||
          selectedCategory === "" ||
          selectedCategory === category;

        const matchSearch = !searchTerm || itemName.includes(searchTerm);

        if (matchCategory && matchSearch) {
          item.style.display = "block";
          visibleItems++;
        } else {
          item.style.display = "none";
        }
      });


      section.style.display = visibleItems > 0 ? "block" : "none";
    });
  }

 
  searchButton.addEventListener("click", function (e) {
    e.preventDefault();
    filterMenu();
  });

 
  searchInput.addEventListener("keyup", function (e) {
    if (e.key === "Enter") {
      e.preventDefault();
      filterMenu();
    }
  });

 
  categorySelect.addEventListener("change", filterMenu);

 
  function applyInitialFiltersFromURL() {
    const params = new URLSearchParams(window.location.search);
    const cat = params.get("category");
    const search = params.get("search");

    if (cat) categorySelect.value = cat;
    if (search) searchInput.value = search;

    if (cat || search) filterMenu();
  }

  applyInitialFiltersFromURL();
});


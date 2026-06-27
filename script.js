// Mobile navigation toggle
(function () {
  var toggle = document.querySelector(".nav-toggle");
  var links = document.getElementById("navLinks");
  if (!toggle || !links) return;

  toggle.addEventListener("click", function () {
    var open = links.classList.toggle("open");
    toggle.setAttribute("aria-expanded", open ? "true" : "false");
  });

  // Close menu when a link is tapped (mobile)
  links.addEventListener("click", function (e) {
    if (e.target.tagName === "A") {
      links.classList.remove("open");
      toggle.setAttribute("aria-expanded", "false");
    }
  });
})();

// Dark mode toggle (initial theme is set by an inline script in <head>)
(function () {
  var btn = document.getElementById("themeToggle");
  if (!btn) return;

  btn.addEventListener("click", function () {
    var current = document.documentElement.getAttribute("data-theme");
    var next = current === "dark" ? "light" : "dark";
    document.documentElement.setAttribute("data-theme", next);
    try {
      localStorage.setItem("theme", next);
    } catch (e) {}
  });
})();

// Scroll reveal: fade/slide blocks in as they enter the viewport
(function () {
  var reveals = [].slice.call(document.querySelectorAll(".reveal"));
  if (!reveals.length) return;

  var reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  // No animation support (or user prefers reduced motion): just show everything
  if (reduce || !("IntersectionObserver" in window)) {
    reveals.forEach(function (el) {
      el.classList.add("is-visible");
    });
    return;
  }

  var observer = new IntersectionObserver(
    function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add("is-visible");
          observer.unobserve(entry.target);
        }
      });
    },
    { threshold: 0.1, rootMargin: "0px 0px -8% 0px" }
  );

  reveals.forEach(function (el) {
    observer.observe(el);
  });
})();



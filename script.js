// Mobile navigation stays usable without JavaScript; collapse only after setup.
(function () {
  var toggle = document.querySelector(".nav-toggle");
  var links = document.getElementById("navLinks");
  if (!toggle || !links) return;

  function setOpen(open) {
    links.classList.toggle("open", open);
    toggle.setAttribute("aria-expanded", String(open));
    toggle.setAttribute("aria-label", open ? "Close menu" : "Open menu");
  }

  toggle.addEventListener("click", function () {
    var open = toggle.getAttribute("aria-expanded") !== "true";
    setOpen(open);
    if (open) links.querySelector("a").focus();
  });

  links.addEventListener("click", function (event) {
    if (event.target.closest("a")) setOpen(false);
  });

  document.addEventListener("keydown", function (event) {
    if (event.key === "Escape" && links.classList.contains("open")) {
      setOpen(false);
      toggle.focus();
    }
  });

  document.addEventListener("click", function (event) {
    if (!links.contains(event.target) && !toggle.contains(event.target)) setOpen(false);
  });

  document.addEventListener("focusin", function (event) {
    if (!links.contains(event.target) && !toggle.contains(event.target)) setOpen(false);
  });

  var mobile = window.matchMedia("(max-width: 760px)");
  mobile.addEventListener("change", function () {
    if (mobile.matches && links.contains(document.activeElement)) toggle.focus();
    setOpen(false);
  });

  document.documentElement.classList.add("nav-ready");
})();

// Keep the theme control's accessible name, state, and browser chrome in sync.
(function () {
  var button = document.getElementById("themeToggle");
  var meta = document.querySelector('meta[name="theme-color"]');
  if (!button) return;

  function syncTheme() {
    var dark = document.documentElement.getAttribute("data-theme") === "dark";
    var label = dark ? "Switch to light mode" : "Switch to dark mode";
    button.setAttribute("aria-label", label);
    button.setAttribute("title", label);
    button.setAttribute("aria-pressed", String(dark));
    if (meta) meta.setAttribute("content", dark ? "#181714" : "#fcfbf8");
  }

  button.addEventListener("click", function () {
    var current = document.documentElement.getAttribute("data-theme");
    var next = current === "dark" ? "light" : "dark";
    document.documentElement.setAttribute("data-theme", next);
    try { localStorage.setItem("theme", next); } catch (e) {}
    syncTheme();
  });

  syncTheme();
  document.documentElement.classList.add("theme-ready");
})();

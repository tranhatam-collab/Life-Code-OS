(function () {
  "use strict";

  var doc = document;
  var body = doc.body;

  var menuToggle = doc.getElementById("lcMenuToggle");
  var nav = doc.getElementById("lcNav");
  var header = doc.querySelector(".lc-header");

  function safeQueryAll(selector) {
    return Array.prototype.slice.call(doc.querySelectorAll(selector));
  }

  function closeMenu() {
    if (!menuToggle || !nav) return;
    menuToggle.setAttribute("aria-expanded", "false");
    nav.classList.remove("is-open");
    body.classList.remove("lc-menu-open");
  }

  function openMenu() {
    if (!menuToggle || !nav) return;
    menuToggle.setAttribute("aria-expanded", "true");
    nav.classList.add("is-open");
    body.classList.add("lc-menu-open");
  }

  function toggleMenu() {
    if (!menuToggle || !nav) return;
    var isExpanded = menuToggle.getAttribute("aria-expanded") === "true";
    if (isExpanded) {
      closeMenu();
    } else {
      openMenu();
    }
  }

  function bindMenu() {
    if (!menuToggle || !nav) return;

    menuToggle.addEventListener("click", toggleMenu);

    safeQueryAll("#lcNav a").forEach(function (link) {
      link.addEventListener("click", function () {
        closeMenu();
      });
    });

    doc.addEventListener("click", function (event) {
      if (!nav.classList.contains("is-open")) return;
      if (nav.contains(event.target) || menuToggle.contains(event.target)) return;
      closeMenu();
    });

    window.addEventListener("resize", function () {
      if (window.innerWidth > 980) {
        closeMenu();
      }
    });

    doc.addEventListener("keydown", function (event) {
      if (event.key === "Escape") {
        closeMenu();
      }
    });
  }

  function setCurrentNavState() {
    var path = window.location.pathname || "/";
    var links = safeQueryAll("#lcNav a, .lc-footer a");

    links.forEach(function (link) {
      var href = link.getAttribute("href");
      if (!href) return;

      if (href === path) {
        link.classList.add("is-current");
      }

      if (path === "/" && href === "/") {
        link.classList.add("is-current");
      }
    });
  }

  function initHeaderScrollState() {
    if (!header) return;

    function onScroll() {
      if (window.scrollY > 8) {
        header.classList.add("lc-header-scrolled");
      } else {
        header.classList.remove("lc-header-scrolled");
      }
    }

    onScroll();
    window.addEventListener("scroll", onScroll, { passive: true });
  }

  function initRevealCards() {
    var items = safeQueryAll(
      ".lc-card, .lc-level-card, .lc-link-card, .lc-roadmap-item, .mini-card, .lc-panel-item, .lc-stat-box, .lc-strip-item"
    );

    if (!("IntersectionObserver" in window) || !items.length) {
      items.forEach(function (item) {
        item.classList.add("lc-revealed");
      });
      return;
    }

    var observer = new IntersectionObserver(
      function (entries) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting) {
            entry.target.classList.add("lc-revealed");
            observer.unobserve(entry.target);
          }
        });
      },
      {
        rootMargin: "0px 0px -40px 0px",
        threshold: 0.08
      }
    );

    items.forEach(function (item, index) {
      item.style.setProperty("--lc-delay", String((index % 6) * 40) + "ms");
      observer.observe(item);
    });
  }

  function initSmoothInternalLinks() {
    safeQueryAll('a[href^="#"]').forEach(function (anchor) {
      anchor.addEventListener("click", function (event) {
        var href = anchor.getAttribute("href");
        if (!href || href === "#") return;

        var target = doc.querySelector(href);
        if (!target) return;

        event.preventDefault();

        var headerOffset = header ? header.offsetHeight + 10 : 0;
        var targetTop = target.getBoundingClientRect().top + window.scrollY - headerOffset;

        window.scrollTo({
          top: targetTop,
          behavior: "smooth"
        });

        closeMenu();
      });
    });
  }

  function initExternalLinks() {
    safeQueryAll('a[target="_blank"]').forEach(function (link) {
      var rel = link.getAttribute("rel") || "";
      if (!/noopener/.test(rel)) {
        link.setAttribute("rel", "noopener noreferrer");
      }
    });
  }

  function initPageState() {
    body.classList.add("lc-ready");
  }

  function boot() {
    bindMenu();
    setCurrentNavState();
    initHeaderScrollState();
    initRevealCards();
    initSmoothInternalLinks();
    initExternalLinks();
    initPageState();
  }

  if (doc.readyState === "loading") {
    doc.addEventListener("DOMContentLoaded", boot);
  } else {
    boot();
  }
})();

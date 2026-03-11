(function () {
  const menuToggle = document.getElementById('menuToggle');
  const siteNav = document.getElementById('siteNav');

  if (menuToggle && siteNav) {
    menuToggle.addEventListener('click', function () {
      const isExpanded = menuToggle.getAttribute('aria-expanded') === 'true';
      menuToggle.setAttribute('aria-expanded', String(!isExpanded));
      siteNav.classList.toggle('is-open');
    });

    siteNav.querySelectorAll('a').forEach(function (link) {
      link.addEventListener('click', function () {
        menuToggle.setAttribute('aria-expanded', 'false');
        siteNav.classList.remove('is-open');
      });
    });
  }

  document.querySelectorAll('a[href^="#"]').forEach(function (anchor) {
    anchor.addEventListener('click', function (event) {
      const href = anchor.getAttribute('href');
      if (!href || href === '#') return;

      const target = document.querySelector(href);
      if (!target) return;

      event.preventDefault();
      target.scrollIntoView({
        behavior: 'smooth',
        block: 'start'
      });
    });
  });
})();

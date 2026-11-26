// Native details keeps navigation usable without JavaScript.
(() => {
  const menu = document.querySelector('.main-menu');
  if (!menu) return;
  const mobile = window.matchMedia('(max-width: 760px)');
  const adapt = () => { menu.open = !mobile.matches; };
  adapt();
  mobile.addEventListener('change', adapt);
  menu.addEventListener('keydown', event => {
    if (event.key === 'Escape' && mobile.matches && menu.open) {
      menu.open = false;
      menu.querySelector('summary').focus();
    }
  });
})();

// NamDU Xalqaro Bo'lim — JavaScript

document.addEventListener('DOMContentLoaded', function () {

  // ===== STICKY HEADER =====
  const header = document.querySelector('.edu-header');
  if (header) {
    window.addEventListener('scroll', () => {
      header.classList.toggle('sticky', window.scrollY > 80);
    });
  }

  // ===== MOBILE MENU =====
  const toggle = document.getElementById('mobileMenuToggle');
  const overlay = document.getElementById('mobileMenuOverlay');
  const nav = document.getElementById('mobileNav');
  const close = document.getElementById('mobileNavClose');

  function openMenu() {
    nav && nav.classList.add('open');
    overlay && overlay.classList.add('open');
    document.body.style.overflow = 'hidden';
  }

  function closeMenu() {
    nav && nav.classList.remove('open');
    overlay && overlay.classList.remove('open');
    document.body.style.overflow = '';
  }

  toggle && toggle.addEventListener('click', openMenu);
  close && close.addEventListener('click', closeMenu);
  overlay && overlay.addEventListener('click', closeMenu);

  // ===== COUNTER ANIMATION =====
  function animateCounter(el) {
    const target = parseInt(el.dataset.target || el.textContent, 10);
    if (isNaN(target)) return;
    const suffix = el.dataset.suffix || '';
    const duration = 2000;
    const step = target / (duration / 16);
    let current = 0;

    const timer = setInterval(() => {
      current += step;
      if (current >= target) {
        el.textContent = target.toLocaleString() + suffix;
        clearInterval(timer);
      } else {
        el.textContent = Math.floor(current).toLocaleString() + suffix;
      }
    }, 16);
  }

  const counterObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting && !entry.target.dataset.animated) {
        entry.target.dataset.animated = 'true';
        animateCounter(entry.target);
      }
    });
  }, { threshold: 0.5 });

  document.querySelectorAll('.count-number, .stat-number').forEach(el => {
    const val = el.textContent.replace(/[^0-9]/g, '');
    if (val) {
      el.dataset.target = val;
      counterObserver.observe(el);
    }
  });

  // ===== SCROLL REVEAL =====
  const revealObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('revealed');
        revealObserver.unobserve(entry.target);
      }
    });
  }, { threshold: 0.1 });

  document.querySelectorAll('[data-sal]').forEach(el => {
    el.classList.add('sal-hidden');
    revealObserver.observe(el);
  });

  // ===== TABS =====
  document.querySelectorAll('.tab-btn').forEach(btn => {
    btn.addEventListener('click', function () {
      const group = this.closest('[data-tab-group]') || this.parentElement;
      const target = this.dataset.tab;

      group.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active'));
      this.classList.add('active');

      if (target) {
        document.querySelectorAll('[data-tab-content]').forEach(c => {
          c.style.display = c.dataset.tabContent === target ? 'block' : 'none';
        });
      }
    });
  });

});

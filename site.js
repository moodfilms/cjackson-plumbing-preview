(function () {
  // Mobile menu
  var menuBtn = document.querySelector('.menu-btn');
  var nav = document.getElementById('site-nav');
  if (menuBtn && nav) {
    var setMenu = function (open) {
      menuBtn.setAttribute('aria-expanded', String(open));
      menuBtn.setAttribute('aria-label', open ? 'Close menu' : 'Open menu');
      nav.classList.toggle('is-open', open);
    };
    menuBtn.addEventListener('click', function () {
      setMenu(menuBtn.getAttribute('aria-expanded') !== 'true');
    });
    nav.querySelectorAll('a').forEach(function (a) {
      a.addEventListener('click', function () { setMenu(false); });
    });
    document.addEventListener('keydown', function (e) { if (e.key === 'Escape') setMenu(false); });
  }

  // Project viewer tabs (homepage)
  var tablist = document.querySelector('.viewer-tabs[role="tablist"]');
  if (tablist) {
    var tabs = Array.prototype.slice.call(tablist.querySelectorAll('[role="tab"]'));
    var select = function (tab) {
      tabs.forEach(function (t) {
        var on = t === tab;
        t.setAttribute('aria-selected', String(on));
        t.tabIndex = on ? 0 : -1;
        document.getElementById(t.getAttribute('aria-controls')).hidden = !on;
      });
    };
    tabs.forEach(function (tab, i) {
      tab.addEventListener('click', function () { select(tab); });
      tab.addEventListener('keydown', function (e) {
        var j = null;
        if (e.key === 'ArrowRight') j = (i + 1) % tabs.length;
        if (e.key === 'ArrowLeft') j = (i - 1 + tabs.length) % tabs.length;
        if (e.key === 'Home') j = 0;
        if (e.key === 'End') j = tabs.length - 1;
        if (j !== null) { e.preventDefault(); tabs[j].focus(); select(tabs[j]); }
      });
    });
  }

  // Quote form: opens the visitor's email app with the details filled in.
  // Swap this for a form service (Formspree, Netlify Forms, etc.) when the site goes live.
  var form = document.getElementById('quote-form');
  if (form) {
    var status = document.getElementById('form-status');
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      if (!form.reportValidity()) return;
      var d = new FormData(form);
      var subject = 'Quote request: ' + d.get('job') + ' (' + d.get('postcode') + ')';
      var body = [
        'Name: ' + d.get('name'),
        'Phone: ' + d.get('phone'),
        'Email: ' + (d.get('email') || 'not given'),
        'Postcode: ' + d.get('postcode'),
        'Type of job: ' + d.get('job'),
        '',
        d.get('message')
      ].join('\n');
      window.location.href = 'mailto:cjacksonplumbing@hotmail.com?subject=' +
        encodeURIComponent(subject) + '&body=' + encodeURIComponent(body);
      status.hidden = false;
    });
  }

  // Lightbox (work page)
  var dlg = document.getElementById('lightbox');
  if (dlg && typeof dlg.showModal === 'function') {
    var img = dlg.querySelector('img');
    var cap = dlg.querySelector('figcaption');
    document.querySelectorAll('[data-full]').forEach(function (btn) {
      btn.addEventListener('click', function () {
        img.src = btn.getAttribute('data-full');
        img.alt = btn.querySelector('img').alt;
        cap.textContent = btn.getAttribute('data-caption') || '';
        dlg.showModal();
      });
    });
    dlg.addEventListener('click', function (e) {
      if (e.target === dlg || e.target.closest('.lb-close')) dlg.close();
    });
  }
})();

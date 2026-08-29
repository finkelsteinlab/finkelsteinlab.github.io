/* Hover cards for links listed in _data/link_previews.yml.
 *
 * The data is embedded in the page by _includes/blog/link-previews.html as
 * a JSON script block, keyed by URL. Any <a> inside .blog-content whose href
 * matches a key gets a card on hover and keyboard focus. Everything is
 * static and self-hosted: the CSP forbids fetching from other origins, so
 * there is no live unfurling.
 */
(function () {
  'use strict';

  var dataEl = document.getElementById('link-previews-data');
  if (!dataEl) return;

  var previews;
  try {
    previews = JSON.parse(dataEl.textContent);
  } catch (e) {
    return;
  }

  // Normalise so "https://x.org/a/" and "https://x.org/a" match.
  function key(url) {
    return url.replace(/\/+$/, '').replace(/^http:/, 'https:');
  }
  var byUrl = {};
  Object.keys(previews).forEach(function (u) { byUrl[key(u)] = previews[u]; });

  var card = document.createElement('div');
  card.className = 'link-preview';
  card.setAttribute('role', 'tooltip');
  card.hidden = true;
  document.body.appendChild(card);

  var hideTimer = null;
  var current = null;

  function render(p) {
    card.innerHTML = '';
    if (p.image) {
      var img = document.createElement('img');
      img.src = p.image;
      img.alt = '';
      card.appendChild(img);
    }
    var body = document.createElement('div');
    body.className = 'link-preview-body';
    if (p.site) {
      var site = document.createElement('div');
      site.className = 'link-preview-site';
      site.textContent = p.site;
      body.appendChild(site);
    }
    var title = document.createElement('div');
    title.className = 'link-preview-title';
    title.textContent = p.title || '';
    body.appendChild(title);
    if (p.description) {
      var desc = document.createElement('div');
      desc.className = 'link-preview-desc';
      desc.textContent = p.description;
      body.appendChild(desc);
    }
    card.appendChild(body);
  }

  function place(link) {
    var r = link.getBoundingClientRect();
    var margin = 8;
    card.hidden = false;
    var cw = card.offsetWidth;
    var ch = card.offsetHeight;
    var left = r.left + window.scrollX;
    var maxLeft = window.scrollX + document.documentElement.clientWidth - cw - margin;
    if (left > maxLeft) left = maxLeft;
    if (left < window.scrollX + margin) left = window.scrollX + margin;
    var top = r.bottom + window.scrollY + margin;
    var below = document.documentElement.clientHeight - r.bottom;
    if (below < ch + margin && r.top > ch + margin) {
      top = r.top + window.scrollY - ch - margin;
    }
    card.style.left = left + 'px';
    card.style.top = top + 'px';
  }

  function show(link) {
    clearTimeout(hideTimer);
    if (current === link && !card.hidden) return;
    current = link;
    render(byUrl[key(link.href)]);
    place(link);
  }

  function hide() {
    hideTimer = setTimeout(function () {
      card.hidden = true;
      current = null;
    }, 150);
  }

  card.addEventListener('mouseenter', function () { clearTimeout(hideTimer); });
  card.addEventListener('mouseleave', hide);

  var links = document.querySelectorAll('.blog-content a[href]');
  Array.prototype.forEach.call(links, function (link) {
    if (!byUrl[key(link.href)]) return;
    link.classList.add('has-preview');
    link.addEventListener('mouseenter', function () { show(link); });
    link.addEventListener('mouseleave', hide);
    link.addEventListener('focus', function () { show(link); });
    link.addEventListener('blur', hide);
  });

  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape') { card.hidden = true; current = null; }
  });
})();

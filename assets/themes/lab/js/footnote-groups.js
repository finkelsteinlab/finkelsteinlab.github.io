/*
 * Collapse runs of adjacent footnote references into a journal-style group.
 *
 * Kramdown renders `text[^2][^3][^4][^5][^7]` as five separate <sup>
 * elements with nothing between them, so the page reads "23457". This
 * rewrites each run into a single <sup> reading "2-5,7", with the numbers
 * sorted and consecutive stretches of three or more turned into a range.
 *
 * Why client-side: GitHub Pages builds in safe mode, so a Jekyll plugin
 * cannot run, and the numbering does not exist until Kramdown assigns it.
 * The markup is correct without this script; it only reformats.
 *
 * Every original id is preserved. A number that a range swallows keeps its
 * id on an empty inline <span> inside the group, so the reverse-footnote
 * links at the bottom of the post still land on the right citation.
 */
(function () {
  'use strict';

  var RANGE_DASH = '–'; // en dash
  var MIN_RANGE = 3; // 2,3 stays "2,3"; 2,3,4 becomes "2-4"

  function isSkippable(node) {
    return node.nodeType === Node.TEXT_NODE && !/\S/.test(node.nodeValue);
  }

  function isFootnoteRef(node) {
    return (
      node.nodeType === Node.ELEMENT_NODE &&
      node.tagName === 'SUP' &&
      node.getAttribute('role') === 'doc-noteref' &&
      node.querySelector('a.footnote')
    );
  }

  /* Walk forward from a <sup>, collecting the run it starts. Whitespace
     between references is absorbed; any other content ends the run. */
  function collectRun(first) {
    var run = [first];
    var spent = [];
    var node = first.nextSibling;
    while (node) {
      if (isSkippable(node)) {
        spent.push(node);
        node = node.nextSibling;
      } else if (isFootnoteRef(node)) {
        run.push(node);
        node = node.nextSibling;
      } else {
        break;
      }
    }
    return { refs: run, whitespace: spent };
  }

  function describe(sup) {
    var link = sup.querySelector('a.footnote');
    var n = parseInt(link.textContent.trim(), 10);
    return {
      n: isNaN(n) ? null : n,
      href: link.getAttribute('href'),
      id: sup.getAttribute('id'),
      sup: sup
    };
  }

  function marker(id) {
    var span = document.createElement('span');
    span.id = id;
    span.className = 'footnote-group-anchor';
    return span;
  }

  function link(ref) {
    var a = document.createElement('a');
    a.href = ref.href;
    a.className = 'footnote';
    a.rel = 'footnote';
    a.textContent = String(ref.n);
    if (ref.id) a.id = ref.id; // keep the reverse-footnote target working
    return a;
  }

  /* Split ascending numbers into consecutive stretches. */
  function segment(refs) {
    var out = [];
    var current = [refs[0]];
    for (var i = 1; i < refs.length; i++) {
      if (refs[i].n === refs[i - 1].n + 1) {
        current.push(refs[i]);
      } else {
        out.push(current);
        current = [refs[i]];
      }
    }
    out.push(current);
    return out;
  }

  function build(refs, orphanIds) {
    var sup = document.createElement('sup');
    sup.className = 'footnote-group';
    sup.setAttribute('role', 'doc-noteref');

    segment(refs).forEach(function (stretch, index) {
      if (index > 0) sup.appendChild(document.createTextNode(','));

      if (stretch.length >= MIN_RANGE) {
        sup.appendChild(link(stretch[0]));
        // The numbers the dash hides still need their ids on the page.
        for (var i = 1; i < stretch.length - 1; i++) {
          if (stretch[i].id) sup.appendChild(marker(stretch[i].id));
        }
        sup.appendChild(document.createTextNode(RANGE_DASH));
        sup.appendChild(link(stretch[stretch.length - 1]));
      } else {
        stretch.forEach(function (ref, i) {
          if (i > 0) sup.appendChild(document.createTextNode(','));
          sup.appendChild(link(ref));
        });
      }
    });

    orphanIds.forEach(function (id) {
      sup.appendChild(marker(id));
    });

    return sup;
  }

  function collapse(root) {
    var sups = Array.prototype.slice.call(
      root.querySelectorAll('sup[role="doc-noteref"]')
    );
    var handled = new Set();

    sups.forEach(function (sup) {
      if (handled.has(sup)) return;

      var run = collectRun(sup);
      run.refs.forEach(function (node) {
        handled.add(node);
      });
      if (run.refs.length < 2) return;

      var refs = run.refs.map(describe);
      if (
        refs.some(function (ref) {
          return ref.n === null;
        })
      ) {
        return; // not numeric; leave the run alone
      }

      refs.sort(function (a, b) {
        return a.n - b.n;
      });

      // A number cited twice in one run shows once, but keeps both ids.
      var unique = [];
      var orphanIds = [];
      refs.forEach(function (ref) {
        if (unique.length && unique[unique.length - 1].n === ref.n) {
          if (ref.id) orphanIds.push(ref.id);
        } else {
          unique.push(ref);
        }
      });

      var group = build(unique, orphanIds);
      sup.parentNode.insertBefore(group, sup);
      run.refs.forEach(function (node) {
        node.remove();
      });
      run.whitespace.forEach(function (node) {
        node.remove();
      });
    });
  }

  function init() {
    var article = document.querySelector('.blog-content');
    if (article) collapse(article);
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();

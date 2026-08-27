/**
 * Theme Toggle for Finkelstein Lab Website
 * Supports light/dark modes with system preference detection.
 *
 * Every localStorage access is wrapped in try/catch: in Safari with "Block All
 * Cookies", or any browser with site data blocked, even *reading* localStorage
 * throws SecurityError. Previously that exception escaped the IIFE and neither
 * the theme nor the toggle button was ever wired up, so the button rendered and
 * did nothing. Now storage failure degrades to a session-only toggle backed by
 * the prefers-color-scheme media query.
 *
 * This file is loaded with `defer`, so it runs after <body> has parsed but
 * before DOMContentLoaded. theme.css carries a matching
 * `@media (prefers-color-scheme: dark)` block, so a user whose OS preference
 * matches their stored preference (or who has no stored preference) sees the
 * right theme painted by CSS with no flash.
 */

(function() {
  'use strict';

  var STORAGE_KEY = 'theme-preference';

  /**
   * Read the stored preference. Returns null if storage is unavailable,
   * blocked, or empty.
   */
  function readStoredTheme() {
    try {
      var stored = window.localStorage.getItem(STORAGE_KEY);
      return (stored === 'dark' || stored === 'light') ? stored : null;
    } catch (e) {
      return null;
    }
  }

  /**
   * Persist the preference. Returns true on success, false if storage threw.
   * Callers must treat failure as non-fatal.
   */
  function writeStoredTheme(theme) {
    try {
      window.localStorage.setItem(STORAGE_KEY, theme);
      return true;
    } catch (e) {
      return false;
    }
  }

  /**
   * The OS-level preference, which is also what theme.css falls back to.
   */
  function systemTheme() {
    try {
      if (window.matchMedia &&
          window.matchMedia('(prefers-color-scheme: dark)').matches) {
        return 'dark';
      }
    } catch (e) {
      /* matchMedia is effectively universal, but never let it break init. */
    }
    return 'light';
  }

  /**
   * Get the user's theme preference.
   * Priority: localStorage > system preference > default (light)
   */
  function getPreferredTheme() {
    return readStoredTheme() || systemTheme();
  }

  /**
   * Apply theme to document
   */
  function setTheme(theme) {
    document.documentElement.setAttribute('data-theme', theme);

    // Update giscus theme if present
    try {
      var giscusFrame = document.querySelector('iframe.giscus-frame');
      if (giscusFrame && giscusFrame.contentWindow) {
        giscusFrame.contentWindow.postMessage(
          { giscus: { setConfig: { theme: theme === 'dark' ? 'dark' : 'light' } } },
          'https://giscus.app'
        );
      }
    } catch (e) {
      /* Cross-origin frame not ready yet; harmless. */
    }

    // Update toggle button icon, text and pressed state
    updateToggleButton(theme);
  }

  /**
   * Update the toggle button appearance and ARIA state.
   * aria-pressed reflects whether dark mode is currently engaged.
   */
  function updateToggleButton(theme) {
    var btn = document.querySelector('.theme-toggle');
    if (!btn) return;

    var icon = btn.querySelector('.theme-toggle-icon');
    var text = btn.querySelector('.theme-toggle-text');
    var isDark = (theme === 'dark');

    if (isDark) {
      if (icon) icon.textContent = '☀️';
      if (text) text.textContent = 'Light';
      btn.setAttribute('aria-label', 'Switch to light theme');
    } else {
      if (icon) icon.textContent = '🌙';
      if (text) text.textContent = 'Dark';
      btn.setAttribute('aria-label', 'Switch to dark theme');
    }

    btn.setAttribute('aria-pressed', isDark ? 'true' : 'false');
  }

  /**
   * Toggle between light and dark themes.
   * The theme is applied FIRST and persisted second, so a storage failure
   * degrades to a session-only toggle instead of killing the click.
   */
  function toggleTheme() {
    var current = document.documentElement.getAttribute('data-theme');
    if (current !== 'dark' && current !== 'light') {
      current = systemTheme();
    }
    var next = (current === 'dark') ? 'light' : 'dark';

    setTheme(next);
    writeStoredTheme(next);
  }

  /**
   * Initialize toggle button click handler
   */
  function initToggleButton() {
    var btn = document.querySelector('.theme-toggle');
    if (btn) {
      btn.addEventListener('click', toggleTheme);
      // Sync the button with whatever theme is currently applied; with `defer`
      // the button already exists by the time init() runs, but this also covers
      // the case where the script is moved back into the <head> un-deferred.
      updateToggleButton(
        document.documentElement.getAttribute('data-theme') || systemTheme()
      );
    }
  }

  /**
   * Listen for OS preference changes, but only follow them while the user has
   * made no explicit choice.
   */
  function initSystemListener() {
    if (!window.matchMedia) return;

    var mq;
    try {
      mq = window.matchMedia('(prefers-color-scheme: dark)');
    } catch (e) {
      return;
    }

    var handler = function(e) {
      if (!readStoredTheme()) {
        setTheme(e.matches ? 'dark' : 'light');
      }
    };

    if (typeof mq.addEventListener === 'function') {
      mq.addEventListener('change', handler);
    } else if (typeof mq.addListener === 'function') {
      // Safari < 14
      mq.addListener(handler);
    }
  }

  /**
   * Initialize theme system
   */
  function init() {
    setTheme(getPreferredTheme());

    if (document.readyState === 'loading') {
      document.addEventListener('DOMContentLoaded', initToggleButton);
    } else {
      initToggleButton();
    }

    initSystemListener();
  }

  init();
})();

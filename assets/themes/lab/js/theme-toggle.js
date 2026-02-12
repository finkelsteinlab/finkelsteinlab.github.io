/**
 * Theme Toggle for Finkelstein Lab Website
 * Supports light/dark modes with system preference detection
 */

(function() {
  'use strict';

  const STORAGE_KEY = 'theme-preference';
  
  /**
   * Get the user's theme preference
   * Priority: localStorage > system preference > default (light)
   */
  function getPreferredTheme() {
    const stored = localStorage.getItem(STORAGE_KEY);
    if (stored) {
      return stored;
    }
    
    // Check system preference
    if (window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches) {
      return 'dark';
    }
    
    return 'light';
  }
  
  /**
   * Apply theme to document
   */
  function setTheme(theme) {
    document.documentElement.setAttribute('data-theme', theme);
    
    // Update giscus theme if present
    const giscusFrame = document.querySelector('iframe.giscus-frame');
    if (giscusFrame) {
      giscusFrame.contentWindow.postMessage(
        { giscus: { setConfig: { theme: theme === 'dark' ? 'dark' : 'light' } } },
        'https://giscus.app'
      );
    }
    
    // Update toggle button icon and text
    updateToggleButton(theme);
  }
  
  /**
   * Update the toggle button appearance
   */
  function updateToggleButton(theme) {
    const btn = document.querySelector('.theme-toggle');
    if (!btn) return;
    
    const icon = btn.querySelector('.theme-toggle-icon');
    const text = btn.querySelector('.theme-toggle-text');
    
    if (theme === 'dark') {
      if (icon) icon.textContent = '☀️';
      if (text) text.textContent = 'Light';
      btn.setAttribute('aria-label', 'Switch to light theme');
    } else {
      if (icon) icon.textContent = '🌙';
      if (text) text.textContent = 'Dark';
      btn.setAttribute('aria-label', 'Switch to dark theme');
    }
  }
  
  /**
   * Toggle between light and dark themes
   */
  function toggleTheme() {
    const current = document.documentElement.getAttribute('data-theme') || 'light';
    const next = current === 'dark' ? 'light' : 'dark';
    
    localStorage.setItem(STORAGE_KEY, next);
    setTheme(next);
  }
  
  /**
   * Initialize toggle button click handler
   */
  function initToggleButton() {
    const btn = document.querySelector('.theme-toggle');
    if (btn) {
      btn.addEventListener('click', toggleTheme);
    }
  }
  
  /**
   * Initialize theme system
   */
  function init() {
    // Apply theme immediately (before DOM ready to prevent flash)
    const theme = getPreferredTheme();
    setTheme(theme);
    
    // Initialize button when DOM is ready
    if (document.readyState === 'loading') {
      document.addEventListener('DOMContentLoaded', initToggleButton);
    } else {
      initToggleButton();
    }
    
    // Listen for system preference changes
    if (window.matchMedia) {
      window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', (e) => {
        // Only auto-switch if user hasn't set a preference
        if (!localStorage.getItem(STORAGE_KEY)) {
          setTheme(e.matches ? 'dark' : 'light');
        }
      });
    }
  }
  
  // Run immediately
  init();
})();

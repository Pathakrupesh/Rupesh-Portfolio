/**
 * Rupesh Portfolio — JavaScript Functionality
 * Includes Theme Toggle (Dark/Light mode) & Client-side Project Filtering
 */

document.addEventListener('DOMContentLoaded', () => {
    // --------------------------------------------------------------------------
    // 1. Theme Management (Dark Mode Default + LocalStorage UI Preference)
    // --------------------------------------------------------------------------
    const themeToggleBtn = document.getElementById('themeToggleBtn');
    const htmlElement = document.documentElement;
    const lightIcon = document.querySelector('.theme-icon-light');
    const darkIcon = document.querySelector('.theme-icon-dark');

    // Retrieve stored theme or default to 'dark'
    const currentTheme = localStorage.getItem('rupesh_theme') || 'dark';
    applyTheme(currentTheme);

    if (themeToggleBtn) {
        themeToggleBtn.addEventListener('click', () => {
            const current = htmlElement.getAttribute('data-bs-theme');
            const newTheme = current === 'dark' ? 'light' : 'dark';
            applyTheme(newTheme);
            localStorage.setItem('rupesh_theme', newTheme);
        });
    }

    function applyTheme(theme) {
        htmlElement.setAttribute('data-bs-theme', theme);
        if (theme === 'light') {
            if (lightIcon) lightIcon.classList.remove('d-none');
            if (darkIcon) darkIcon.classList.add('d-none');
        } else {
            if (lightIcon) lightIcon.classList.add('d-none');
            if (darkIcon) darkIcon.classList.remove('d-none');
        }
    }

    // --------------------------------------------------------------------------
    // 2. Client-Side Instant Project Filtering (No page reload)
    // --------------------------------------------------------------------------
    const filterButtons = document.querySelectorAll('.btn-filter');
    const projectItems = document.querySelectorAll('.project-item');
    const noFilterMatch = document.getElementById('noFilterMatch');

    if (filterButtons.length > 0 && projectItems.length > 0) {
        filterButtons.forEach(btn => {
            btn.addEventListener('click', (e) => {
                const targetFilter = btn.getAttribute('data-filter');

                // Update active button state
                filterButtons.forEach(b => b.classList.remove('active'));
                btn.classList.add('active');

                let visibleCount = 0;

                projectItems.forEach(item => {
                    const category = item.getAttribute('data-category');
                    if (targetFilter === 'all' || category === targetFilter) {
                        item.style.display = 'block';
                        visibleCount++;
                    } else {
                        item.style.display = 'none';
                    }
                });

                if (noFilterMatch) {
                    if (visibleCount === 0) {
                        noFilterMatch.classList.remove('d-none');
                    } else {
                        noFilterMatch.classList.add('d-none');
                    }
                }
            });
        });
    }

    // --------------------------------------------------------------------------
    // 3. Auto-Dismiss Alert Messages after 6 seconds
    // --------------------------------------------------------------------------
    const alerts = document.querySelectorAll('.alert-dismissible');
    alerts.forEach(alert => {
        setTimeout(() => {
            const bsAlert = bootstrap.Alert.getOrCreateInstance(alert);
            if (bsAlert) {
                bsAlert.close();
            }
        }, 6000);
    });
});

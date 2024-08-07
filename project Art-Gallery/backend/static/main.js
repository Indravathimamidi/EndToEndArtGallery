const themeButton = document.getElementById('theme-button');
const navToggle = document.getElementById('nav-toggle');

// Example event listener for theme change
themeButton.addEventListener('click', () => {
    // Your theme change logic here
    document.body.classList.toggle('dark-theme');
});

// Example event listener for nav toggle
navToggle.addEventListener('click', () => {
    // Your navigation toggle logic here
    document.querySelector('.nav_menu').classList.toggle('show-menu');
});

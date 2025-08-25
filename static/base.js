// Slide bar
function toggleSidebar() {
    const sidebar = document.getElementById('sidebar');
    const overlay = document.getElementById('overlay');
    
    // Toggle active class for sidebar and overlay
    sidebar.classList.toggle('active');
    overlay.classList.toggle('active');
}

// Close sidebar if clicked anywhere outside the sidebar
document.addEventListener('click', function(event) {
    const sidebar = document.getElementById('sidebar');
    const overlay = document.getElementById('overlay');
    const menuIcon = document.querySelector('.menu-icon');

    // Check if the sidebar is active and the clicked element is outside sidebar and menu icon
    if (sidebar.classList.contains('active') && !sidebar.contains(event.target) && !menuIcon.contains(event.target)) {
        sidebar.classList.remove('active');
        overlay.classList.remove('active');
    }
});

// JavaScript for toggling the password visibility
document.addEventListener('DOMContentLoaded', function () {
    const togglePassword = document.getElementById('togglePassword');
    const passwordInput = document.getElementById('password');

    togglePassword.addEventListener('click', function () {
        // Toggle the type attribute of the password input
        const type = passwordInput.getAttribute('type') === 'password' ? 'text' : 'password';
        passwordInput.setAttribute('type', type);

        // Toggle the eye image (closed eye vs open eye)
        if (type === 'password') {
            togglePassword.src = "/static/closed-eyes.png"; // Change to closed eye image
        } else {
            togglePassword.src = "/static/open-eyes.png"; // Change to open eye image
        }
    });
});
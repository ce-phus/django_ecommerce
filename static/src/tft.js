
document.addEventListener('DOMContentLoaded', function() {
    const userButton = document.getElementById('dropdown-user-button');
    const userDropdown = document.getElementById('dropdown-user');

    userButton.addEventListener('click', () => {
        userDropdown.classList.toggle('hidden');
    });
});
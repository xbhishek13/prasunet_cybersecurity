document.getElementById('password-form').addEventListener('submit', function (e) {
    e.preventDefault();

    const password = document.getElementById('password').value;
    const retypePassword = document.getElementById('retype-password').value;
    const feedback = document.getElementById('feedback');

    //criteria
    const lengthCriteria = password.length >= 8;
    const uppercaseCriteria = /[A-Z]/.test(password);
    const lowercaseCriteria = /[a-z]/.test(password);
    const numberCriteria = /[0-9]/.test(password);
    const specialCharCriteria = /[!@#$%^&*(),.?":{}|<>]/.test(password);

    // Check for match
    if (password !== retypePassword) {
        feedback.textContent = 'Passwords do not match!';
        feedback.style.color = 'red';
    }
    // Check criteria
    else if (!lengthCriteria) {
        feedback.textContent = 'Password must be at least 8 characters long.';
    } else if (!uppercaseCriteria) {
        feedback.textContent = 'Password must contain at least one uppercase letter.';
    } else if (!lowercaseCriteria) {
        feedback.textContent = 'Password must contain at least one lowercase letter.';
    } else if (!numberCriteria) {
        feedback.textContent = 'Password must contain at least one number.';
    } else if (!specialCharCriteria) {
        feedback.textContent = 'Password must contain at least one special character.';
    } else {
        feedback.textContent = 'Password creation successful';
        feedback.style.color = 'green';
    }
});

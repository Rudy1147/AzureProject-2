const registerForm = document.getElementById("registerForm");
const registerButton = document.getElementById("registerButton");
const message = document.getElementById("message");


registerForm.addEventListener("submit", async function(event) {
    event.preventDefault();
    const username = document.getElementById("username").value.trim();
    const password = document.getElementById("password").value;

    // Clear previous message
    message.textContent = "";

    // Disable button while request is running
    registerButton.disabled = true;
    registerButton.textContent = "Creating account...";

    try {
        const response = await fetch("/auth/register", {
            method: "POST",
            headers: {"Content-Type": "application/json"},
            body: JSON.stringify({username: username, password: password})
        });

        const data = await response.json();

        if (!response.ok) {
            message.textContent = data.detail || "Registration failed.";
            return;
        }

        message.textContent = "Account created successfully!";

        /*
            Give the user a moment to see
            the success message.
        */

        setTimeout(function() {window.location.href = "/login";}, 1000);

    } catch (error) {
        console.error("Registration error:", error);
        message.textContent = "Unable to connect to the authentication service.";
    } finally {
        registerButton.disabled = false;
        registerButton.textContent = "Create Account";
    }
});
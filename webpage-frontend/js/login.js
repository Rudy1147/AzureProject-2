const loginForm = document.getElementById("loginForm");
const loginButton = document.getElementById("loginButton");
const message = document.getElementById("message");


loginForm.addEventListener("submit", async function(event) {
    event.preventDefault();
    const username = document.getElementById("username").value.trim();
    const password = document.getElementById("password").value;

    // Clear previous message
    message.textContent = "";

    // Disable button while request is running
    loginButton.disabled = true;
    loginButton.textContent = "Logging in...";

    try {
        const response = await fetch("/auth/login", {
            method: "POST",
            headers: {"Content-Type": "application/json"},
            body: JSON.stringify({username: username, password: password})
        });

        const data = await response.json();

        if (!response.ok) {
            message.textContent = data.detail || "Login failed.";
            return;
        }


        /*
            Login succeeded.
            The Auth Service returned:
                {
                    access_token: "...",
                    token_type: "bearer"
                }
         */

        localStorage.setItem("access_token", data.access_token);
        message.textContent ="Login successful!";

        /*
            Later this can redirect to
            the image-processing application.
         */
        // window.location.href = "/";


    } catch (error) {
        console.error("Login error:", error);
        message.textContent = "Unable to connect to the authentication service.";
    } finally {
        loginButton.disabled = false;
        loginButton.textContent = "Login";
    }
});
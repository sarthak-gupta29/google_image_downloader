const form = document.getElementById("downloadForm");
const spinner = document.getElementById("loadingSpinner");
const messageDiv = document.getElementById("message");

form.onsubmit = function(event) {
    event.preventDefault(); // Prevent the default form submission
    spinner.style.display = "block"; // Show the spinner
    messageDiv.innerHTML = ""; // Clear any previous messages

    const formData = new FormData(form);

    fetch("/submit", {
        method: "POST",
        body: formData
    })
    .then(response => {
        if (response.headers.get("Content-Type") === "application/json") {
            // Local scenario: display message
            return response.json().then(data => {
                spinner.style.display = "none";
                messageDiv.innerHTML = data.message;
            });
        } else {
            // Server scenario: trigger file download
            return response.blob().then(blob => {
                spinner.style.display = "none";
                const url = window.URL.createObjectURL(blob);
                const a = document.createElement('a');
                a.style.display = 'none';
                a.href = url;
                a.download = 'images.zip';
                document.body.appendChild(a);
                a.click();
                window.URL.revokeObjectURL(url);
                messageDiv.innerHTML = "Download complete! Check your downloads folder.";
            });
        }
    })
    .catch(error => {
        spinner.style.display = "none";
        messageDiv.innerHTML = "Error occurred while processing your request.";
        console.error('Error:', error);
    });
};
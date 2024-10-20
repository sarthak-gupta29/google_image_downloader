const form = document.getElementById("downloadForm");
const submitButton = document.getElementById("submitButton");
const spinner = submitButton.querySelector(".spinner");
const buttonText = submitButton.querySelector(".button-text");
const messageDiv = document.getElementById("message");

form.onsubmit = function(event) {
    event.preventDefault();
    startLoading();
    clearMessage();

    const formData = new FormData(form);

    fetch("/submit", {
        method: "POST",
        body: formData
    })
    .then(response => {
        if (response.headers.get("Content-Type") === "application/json") {
            // Local scenario: display message
            return response.json().then(data => {
                stopLoading();
                showMessage(data.message, "success");
            });
        } else {
            // Server scenario: trigger file download
            return response.blob().then(blob => {
                stopLoading();
                const url = window.URL.createObjectURL(blob);
                const a = document.createElement('a');
                a.style.display = 'none';
                a.href = url;
                a.download = 'images.zip';
                document.body.appendChild(a);
                a.click();
                window.URL.revokeObjectURL(url);
                showMessage("Download complete! Check your downloads folder.", "success");
            });
        }
    })
    .catch(error => {
        stopLoading();
        showMessage("Error occurred while processing your request.", "error");
        console.error('Error:', error);
    });
};

function startLoading() {
    submitButton.disabled = true;
    spinner.style.display = "block";
    buttonText.textContent = "Processing...";
}

function stopLoading() {
    submitButton.disabled = false;
    spinner.style.display = "none";
    buttonText.textContent = "Download Images";
}

function showMessage(text, type) {
    messageDiv.textContent = text;
    messageDiv.className = `message ${type}`;
}

function clearMessage() {
    messageDiv.textContent = "";
    messageDiv.className = "message";
}
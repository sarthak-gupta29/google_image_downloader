const form = document.getElementById("downloadForm");
const spinner = document.getElementById("loadingSpinner");
const messageDiv = document.getElementById("message");

form.onsubmit = function(event) {
    event.preventDefault();  // Prevent the default form submission
    spinner.style.display = "block";  // Show the spinner

    const formData = new FormData(form);
    fetch("/submit", {
        method: "POST",
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        spinner.style.display = "none";  // Hide the spinner
        messageDiv.innerHTML = data.message;  // Display success message
    })
    .catch(error => {
        spinner.style.display = "none";  // Hide the spinner if there's an error
        messageDiv.innerHTML = "Error occurred while downloading images.";
    });
};

function previewImage() {
    const fileInput = document.getElementById('fileInput');
    const previewImage = document.getElementById('previewImage');
    const fileName = document.getElementById('fileName');

    if (fileInput.files.length > 0) {
        const file = fileInput.files[0];
        const reader = new FileReader();

        reader.onload = function (e) {
            previewImage.src = e.target.result;
            previewImage.classList.remove("hidden");
            fileName.innerText = "Selected File: " + file.name;
            fileName.classList.remove("hidden");
        };

        reader.readAsDataURL(file);
    } else {
        fileName.innerText = "No file selected";
        previewImage.classList.add("hidden");
    }
}

function uploadFile() {
    const fileInput = document.getElementById('fileInput');
    const resultSection = document.getElementById('resultSection');
    const resultText = document.getElementById('resultText');
    const loadingSpinner = document.getElementById('loadingSpinner');

    if (!fileInput || fileInput.files.length === 0) {
        alert("Please select a file.");
        return;
    }

    const file = fileInput.files[0];
    const formData = new FormData();
    formData.append("image", file);

    // Show result section and spinner
    resultSection.classList.remove("hidden");
    loadingSpinner.classList.remove("hidden");
    resultText.innerText = "Processing...";

    fetch("http://localhost:5000/detect", {
        method: "POST",
        body: formData
    })
    .then(response => {
        if (!response.ok) {
            throw new Error("Network response was not ok");
        }
        return response.json();
    })
    .then(data => {
        loadingSpinner.classList.add("hidden");  // Stop spinner
        resultText.innerText = data.result || "Detection failed.";
    })
    .catch(error => {
        loadingSpinner.classList.add("hidden");  // Stop spinner on error
        resultText.innerText = "Error processing file.";
        console.error("Error:", error);
    });
}

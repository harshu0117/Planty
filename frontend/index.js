const form = document.getElementById("uploadForm");
const resultDiv = document.getElementById("result");

form.addEventListener("submit", async (event) => {
    event.preventDefault();

    const fileInput = document.getElementById("imageInput");
    const file = fileInput.files[0];

    if (!file) {
        resultDiv.innerHTML = "<p>Please select an image file first.</p>";
        return;
    }

    const formData = new FormData();
    formData.append("file", file);

    try {
        resultDiv.innerHTML = "<p>Processing...</p>";

        const response = await fetch("http://localhost:8000/predict", {
            method: "POST",
            body: formData,
        });

        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }

        const data = await response.json();

        // Display the prediction result
        resultDiv.innerHTML = `
            <p><strong>Predicted Class:</strong> ${data.class}</p>
            <p><strong>Confidence:</strong> ${(data.confidence * 100).toFixed(2)}%</p>
        `;
    } catch (error) {
        console.error("Error:", error);
        resultDiv.innerHTML = `<p>Error occurred: ${error.message}</p>`;
    }
});

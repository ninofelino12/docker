document.addEventListener("DOMContentLoaded", function() {
    // Lakukan permintaan HTTP GET untuk mendapatkan file JSON
    fetch("http://127.0.0.1:4000")
        .then(response => response.json())
        .then(data => {
            // Tetapkan data JSON ke variabel Alpine.js
            Alpine.data('jsonData', data);
        })
        .catch(error => console.error('Error fetching JSON:', error));
});
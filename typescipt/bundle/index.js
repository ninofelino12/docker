"use strict";
console.log('hello');
function ambilFileXML() {
    // Ambil data dari API
    fetch('http://localhost:8015/gateway/arch')
        .then(response => response.text())
        .then(data => {
        var _a;
        console.log(data);
        const parser = new DOMParser();
        const xmlDoc = parser.parseFromString(data, "text/xml");
        const fields = xmlDoc.querySelectorAll("field");
        fields.forEach(field => {
            console.log(field.getAttribute("name"));
        });
        (_a = document.getElementById('id')) === null || _a === void 0 ? void 0 : _a.innerHTML = data;
    })
        .catch(error => console.error(error));
}
// Jalankan fungsi
//ambilFileXML();

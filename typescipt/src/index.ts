console.log('hello');

function ambilFileXML() {
    // Ambil data dari API
    fetch('http://localhost:8015/gateway/arch')
      .then(response => response.text())
      .then(data => {
        console.log(data);
        const parser = new DOMParser();
        const xmlDoc = parser.parseFromString(data, "text/xml");
        const fields = xmlDoc.querySelectorAll("field");
        fields.forEach(field => {
            console.log(field.getAttribute("name"));
        });
        document.getElementById('id')?.innerHTML=data;
      })
      .catch(error => console.error(error));
  }

  // Jalankan fungsi
  //ambilFileXML();
function ambilData(url,tag,type)  {
    // Menggunakan fetch untuk melakukan permintaan HTTP
    fetch(url)
        .then(response => {
            // Memastikan respons dalam format JSON
            document.getElementsByClassName('loader').style.display = 'none'
            if (!response.ok) {
                throw new Error("Gagal mengambil data");
                alert("BUKAN JSON");
            }
            return response.json();
        })
        .then(data => {
            // Menampilkan data ke dalam elemen hasil
            //document.getElementById("hasil").innerHTML=jsonToTable(JSON.parse(data));
            document.getElementById(tag).innerHTML=jsonToTable(data);
            document.getElementsByClassName('loader').style.display = 'none'
          //alert(data)
        })
        ;
}

function jsonToTable(data) {
    const jsonData=data;
    var tableHtml = '<table>';

        // Create table header
        tableHtml += '<thead><tr>';
        for (var key in jsonData[0]) {
            tableHtml += '<th>' + key + '</th>';
        }
        tableHtml += '</tr></thead>';

        // Create table body
        tableHtml += '<tbody>';
        jsonData.forEach(function (obj) {
            tableHtml += '<tr>';
            for (var key in obj) {
                tableHtml += '<td>' + obj[key] + '</td>';
            }
            tableHtml += '</tr>';
        });
        tableHtml += '</tbody>';

        tableHtml += '</table>';
        
        return tableHtml;
  };
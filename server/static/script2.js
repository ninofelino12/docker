function loadAndDisplayJson(url) {
    // Fetch the JSON data
    fetch(url)
      .then(response => 
        // response.json()
        response.text()
        )
      .then(data => {
        // Clear the existing content of the main tag
        document.getElementById('dataContainer').innerHTML = '';
        document.getElementById('dataContainer').innerHTML = jsonToTable(data);
        document.getElementById('log').innerHTML='logdd';
        // Loop through the data and create elements
       
      })
      .catch(error => {
        document.getElementById('dataContainer').innerHTML = error;
        // console.error(error);
        // Handle any errors here, like displaying an error message
      });
  }

  function loadJson(url) {
    // Fetch the JSON data
    fetch(url)
      .then(response => 
        // response.json()
        response.text()
        )
      .then(data => {
        // Clear the existing content of the main tag
        document.getElementById('dataContainer').innerHTML = '';
        document.getElementById('dataContainer').innerHTML = data;
        document.getElementById('log').innerHTML='logdd';
        // Loop through the data and create elements
       
      })
      .catch(error => {
        document.getElementById('dataContainer').innerHTML = error;
        // console.error(error);
        // Handle any errors here, like displaying an error message
      });
  }
  
  function jsonToTable(data) {
    const jsonData=JSON.parse(data);
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
  function getAndDisplayJsonTable(url) {
    // Fetch the JSON data
    fetch(url)
      .then(response => response.json())
      .then(data => {
        // Create and append the table element
        const table = document.createElement('table');
        document.getElementById('your-container-element').appendChild(table);
  
        // Create table header row
        const headerRow = document.createElement('tr');
        headerRow.innerHTML = `<th>ID</th><th>Name</th>`; // Customize header columns based on your data
        table.appendChild(headerRow);
  
        // Loop through each object in the JSON data
        for (const item of data) {
          // Create a table row
          const row = document.createElement('tr');
  
          // Create and fill cells with data
          const idCell = document.createElement('td');
          idCell.textContent = item.id; // Adapt to your data's key-value structure
          row.appendChild(idCell);
  
          const nameCell = document.createElement('td');
          nameCell.textContent = item.name; // Adapt to your data's key-value structure
          row.appendChild(nameCell);
  
          // Add the row to the table
          table.appendChild(row);
        }
      })
      .catch(error => {
        console.error(error);
        // Handle any errors during fetch or parsing
      });
  }
  
  
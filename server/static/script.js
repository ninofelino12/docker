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
        document.getElementById('dataContainer').innerHTML = data;
  
        // Loop through the data and create elements
       
      })
      .catch(error => {
        document.getElementById('dataContainer').innerHTML = error;
        // console.error(error);
        // Handle any errors here, like displaying an error message
      });
  }
  


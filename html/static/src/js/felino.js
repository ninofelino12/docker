document.addEventListener('DOMContentLoaded', function () {
    // Fetch JSON data
    fetch('http://localhost:8015/gateway/api?model=res.partner&items=["name","email","id"]')
                    .then(response => response.json())
                    .then(data => { createCards(data); })
                    .catch(error => console.error('Error fetching JSON:', error));
            });

        function createCards(data) {
            const cardContainer = document.getElementById('card-container');

            // Clear existing cards
            cardContainer.innerHTML = '';
            const domain= window.location.hostname;
            const domainport= window.location.host; 
            var currentDomainWithProtocol = window.location.origin;


            // Iterate through each item in the JSON data
            data.forEach(item => {
                const card = document.createElement('div');
                card.className = 'card';
                    
                // Add content to the card (adjust properties based on your JSON structure)
                card.innerHTML = `
                <div class="bg-gradient-to-r from-indigo-500 to-purple-500 p-1 rounded-lg w-50 min-w-50 max-w-50">
    <img class="rounded-t-lg" src="http://${domain}:8015/gateway/api?type=img&model=res.partner&id=${item.id}" alt="Profile Image">
    <div class="p-5">
        <a href="#" class="block mb-2 text-2xl font-bold tracking-tight text-white dark:text-gray-900">
            ${item.name}
        </a>
        <p class="mb-3 text-sm text-white dark:text-gray-400">
            ${item.email}
        </p>
    </div>
</div>
`
          

            
        ;

                // Append the card to the container
                cardContainer.appendChild(card);
            });
}
function populateTable(data) {
    const tableBody = document.querySelector('#data-table tbody');

    // Clear existing table rows
    tableBody.innerHTML = '';

    // Iterate through each item in the JSON data
    data.forEach(item => {
        const row = document.createElement('li');

        // Add cells for each column in the JSON data
        Object.values(item).forEach(value => {
            const cell = document.createElement('h2');
            cell.textContent = value;
            row.appendChild(cell);
        });

        // Append the row to the table body
        tableBody.appendChild(row);
    });
}

// // Example usage:
// const apiUrl = 'https://api.example.com/data';

// // Call fetchData and store the result in a variable
// const responseData = await fetchData(apiUrl);



async function fetchData(url) {
    try {
      const response = await fetch(url);
      return response.ok ? await response.json() : null;
    } catch (error) {
      console.error('Error fetching data:', error.message);
      return null;
    }
  }
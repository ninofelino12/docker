const odoo = "http://localhost:8015";

fetch('http://localhost:8015/gateway/modelfel?field=id,name')
  .then(response => {
    const headers = response.headers.get('Pragma');
    const fields = ['id', 'name'];
    document.getElementById('judul').innerHTML = headers || fields.join(' ');
  })
  .then(response => response.json())
  .then(jsonData => {
    const hasil = jsonData.map(product => `
      <tr>
        <td>${product.name}</td>
        <td>${product.id}</td>
        <td><img height="10%" src="${odoo}${product.img}" alt="Product Image"></td>
      </tr>
    `).join('');
    document.getElementById('hasil').innerHTML = hasil;
  })
  .catch(error => console.error('Error fetching data:', error));
class Odoo {
    constructor(div) {
      
      this.url='http://localhost:8015';
      this.div='odoo';
      this.card='card';
      this.model='product.product'
      
    }
  
    card(div){
        const html=`
       
        <h2>Features</h2>
        <div class="feature-card mdc-card">
          <div class="feature-icon mdc-card__media"></div>
          <div class="feature-text mdc-card__primary">
            <h3>Feature 1</h3>
            <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p>
          </div>
   
       
        `
        document.getElementById(this.div).innerHTML=html;
    }
  
    getData(endpoint, div) {
          fetch(`http://localhost:8015/gateway/modelfel?field=id,name&model=${this.model}`)
              .then(response => response.json())
              // .then(response => response.json())
              .then(data => {
                  const hasil = data.map(product => `
        <tr>
          <td>${product.name}</td>
          <td>${product.id}</td>
          <td><img width="10%" src="${this.url}${product.img}" alt="Product Image"></td>
        </tr>
      `).join('');
                  document.getElementById(this.div).innerHTML = hasil;
              })
              .catch(); 
  
  
    }
  }
  
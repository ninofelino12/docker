class CardBuilder {
    constructor(containerElement, url) {
      this.containerElement = containerElement;
      this.url = url;
    }
  
    async buildCards() {
      const jsonData = await this.fetchData();
      jsonData.forEach((data) => {
        this.createCard(data);
      });
    }
  
    async fetchData() {
      const response = await fetch(this.url);
      const jsonData = await response.json();
      return jsonData;
    }
  
    createCard(data) {
      const cardElement = document.createElement("div");
      cardElement.classList.add("card");
  
      // Tambahkan konten card
      const imageElement = document.createElement("img");
      imageElement.src = data.image;
      cardElement.appendChild(imageElement);
  
      const titleElement = document.createElement("h3");
      titleElement.textContent = data.title;
      cardElement.appendChild(titleElement);
  
      const descriptionElement = document.createElement("p");
      descriptionElement.textContent = data.description;
      cardElement.appendChild(descriptionElement);
  
      this.containerElement.appendChild(cardElement);
    }
  }
  
  // Contoh penggunaan
  const containerElement = document.getElementById("card-container");
  const url = "https://api.example.com/data.json";
  const cardBuilder = new CardBuilder(containerElement, url);
  cardBuilder.buildCards();

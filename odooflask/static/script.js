const loadJsonLink = document.getElementsByClassName('a')
    const outputDiv = document.getElementById("output");

    loadJsonLink.addEventListener("click", async () => {
 
      try {
        const response = await fetch("http://localhost"); // Replace with your actual JSON URL

        if (!response.ok) {
          throw new Error(`HTTP error ${response.status}`);
        }

        const jsonData = await response.json();
        outputDiv.textContent = JSON.stringify(jsonData, null, 2); // Pretty-print JSON
      } catch (error) {
        console.error("Error fetching JSON:", error);
        outputDiv.textContent = "Error loading JSON data.";
      }
    });
    function clearCache() {
  // Attempt to clear cache using available mechanisms:
  if ('caches' in window) {
    caches.keys().then(cacheNames => {
      return Promise.all(cacheNames.map(cacheName => caches.delete(cacheName)));
    }).then(() => {
      // Cache cleared successfully
      console.log('Cache cleared!');
      // Optionally reload the page:
      window.location.reload();
    });
  } else {
    // Fallback to reloading the page (not as effective as clearing cache)
    window.location.reload();
  }
}
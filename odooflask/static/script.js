async function loadJSON(url,tag) {
  alert('click'+url)
  document.querySelector("#loadButton").style.cursor = "wait";
  document.getElementById("loading-container").style.display = "block";
  var progressBar = document.getElementById("loading-progress-bar");
  progressBar.style.width = "0%";

  try {
    const response = await fetch(url);

    if (!response.ok) {
      throw new Error(`HTTP error! Status: ${response.status}`);
    }

    const data = await response.text();
    document.getElementById(tag).innerHTML = data;
    document.querySelector("#loading-button").style.cursor = "default";
    progressBar.style.width = (100 / data.length) + "%";
    document.getElementById("loading-container").style.display = "none";
    document.getElementById("crd").style.display="none"; 
    return data;
  } catch (error) {
    console.error('Error loading JSON:', error);
    throw error; // Re-throw to allow further handling
  }
}


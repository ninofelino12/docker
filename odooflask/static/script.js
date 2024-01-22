async function loadJSON(url,tag) {
  alert(url+'--------------------'+tag)
  

  try {
    const response = await fetch(url);

    if (!response.ok) {
      throw new Error(`HTTP error! Status: ${response.status}`);
    }

    const data = await response.body;
    document.getElementById(tag).innerHTML = data;
    
    return data;
  } catch (error) {
    console.error('Error loading JSON:', error);
    throw error; // Re-throw to allow further handling
  }
}


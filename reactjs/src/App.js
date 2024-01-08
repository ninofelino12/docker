import './App.css';
import React, { useState, useEffect } from 'react';
// import axios from 'axios';
const server="http://localhost:8015/gateway";



function App() {
  return (
    <div className="App">
      <header className="App-header">
       <h1>Odoo React Js</h1>
       < a href={server}>Odoo</a>
       {/* < a href='${server}/partner'></a> */}
       {JsonDisplayer}
    
      </header>
    </div>
  );
}

function Get_partners(){
  const url=server+'/partner';


 return (
  <pre>partner {url}</pre>
);

}

function JsonDisplayer() {
  const [jsonData, setJsonData] = useState(null);
  const [isLoading, setIsLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await fetch('https://api.example.com/data');
        const data = await response.json();
        setJsonData(data);
      } catch (error) {
        setError(error);
      } finally {
        setIsLoading(false);
      }
    };

    fetchData();
  }, []);
}, []);

  return (
    <div>
      dddd
      {isLoading ? (
        <p>Loading data...</p>
      ) : error ? (
        <p>Error: {error.message}</p>
      ) : (
        <pre>{JSON.stringify(jsonData, null, 2)}</pre>
      )}
    </div>
  );
}

export default App;

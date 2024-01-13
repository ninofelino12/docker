      // Your web app's Firebase configuration
      var firebaseConfig1 = {
        apiKey: "AIzaSyD6rdr3LaXyMTcmP_M2cmqQhwO2JOZEuyc",
        authDomain: "test-dae29.firebaseapp.com",
        databaseURL: "https://test-dae29.firebaseio.com",
        projectId: "test-dae29",
        storageBucket: "test-dae29.appspot.com",
        messagingSenderId: "195245932266",
        appId: "1:195245932266:web:e90f2d7214384be9436193"
      };

      const firebaseConfig = {
        apiKey: "AIzaSyBl1LnJymXg5K6bGQrg4KyoApYvbYGHO4s",
        authDomain: "odoodata-1a010.firebaseapp.com",
        databaseURL: "https://odoodata-1a010-default-rtdb.firebaseio.com",
        projectId: "odoodata-1a010",
        storageBucket: "odoodata-1a010.appspot.com",
        messagingSenderId: "256621005958",
        appId: "1:256621005958:web:b37c55d587b411d36b5507",
        measurementId: "G-7ZPYTEPKSF"
      };
      // Initialize Firebase
      firebase.initializeApp(firebaseConfig);
        
      var firebaseRef = firebase.database().ref().child('login');
      
      firebaseRef.once("value").then(function(snapshot){
        var loginInfo=snapshot.val();
        document.getElementById("login").addEventListener("click",function(){
          var username = document.getElementById("username");
          var password = document.getElementById("pass");
          if (username.value==loginInfo.username && password.value==loginInfo.password){
            location.replace("home.html");
          }else if(username.value!=loginInfo.username){
            username.style.borderColor="red";
          }else if(password.value!=loginInfo.password){
            password.style.borderColor="red";
          }
        });
      });

      document.getElementById('pass').addEventListener("input",function(){
        document.getElementById("pass").style.borderColor="#ccc";
      });
      document.getElementById('username').addEventListener("input",function(){
        document.getElementById("username").style.borderColor="#ccc";
      });
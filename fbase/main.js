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
        
      var firebaseRef = firebase.database().ref().child('data');
     // console.log(firebase.database().ref().child('email'));

      firebaseRef.once("value").then(function(snapshot){
        var loginInfo=snapshot.val();
        console.log(snapshot.val());
      });
      firebase.database().ref('data/'+'isi').set({id:1,nama:'felino',alamat:'bogor'})
     //  console.log(firebaseRe);
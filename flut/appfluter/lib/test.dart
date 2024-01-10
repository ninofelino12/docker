AppBar(
        backgroundColor: Colors.blue,
        title: Text(title, style: const TextStyle(color: Colors.white)),
        actions: [
          IconButton(
              icon: const Icon(Icons.search),
              onPressed: () {
                myUrl = 'http://localhost:8r015/gateway/product//';
                // setState(() {});
                print(myUrl);
                // Add search code here
              }),
          IconButton(
              icon: const Icon(Icons.add),
              onPressed: () {
                // Add widget code here
              }),
          IconButton(
            icon: const Icon(Icons.camera),
            onPressed: () {
              // Add camera button code here
            },
          )
        ],
      ),
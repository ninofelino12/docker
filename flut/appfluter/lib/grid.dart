class MyHomePage extends StatefulWidget {
  @override
  _MyHomePageState createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {
  final TextEditingController _searchController = TextEditingController();
  List<Item> _items = [];
  List<Item> _filteredItems = [];

  @override
  void initState() {
    super.initState();
    fetchData().then((items) {
      setState(() {
        _items = items;
        _filteredItems = items;
      });
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Search Example'),
        bottom: PreferredSize(
          preferredSize: Size.fromHeight(50.0),
          child: Padding(
            padding: EdgeInsets.all(8.0),
            child: TextField(
              controller: _searchController,
              decoration: InputDecoration(
                hintText: 'Search by title...',
                prefixIcon: Icon(Icons.search),
              ),
              onChanged: (query) {
                setState(() {
                  _filteredItems = _items
                      .where((item) => item.title
                          .toLowerCase()
                          .contains(query.toLowerCase()))
                      .toList();
                });
              },
            ),
          ),
        ),
      ),
      body: GridView.builder(
        gridDelegate: SliverGridDelegateWithFixedCrossAxisCount(
          crossAxisCount: 2,
        ),
        itemCount: _filteredItems.length,
        itemBuilder: (context, index) {
          return Card(
            child: Column(
              children: [
                Image.network(_filteredItems[index].imageUrl),
                Text(_filteredItems[index].title),
              ],
            ),
          );
        },
      ),
    );
  }
}

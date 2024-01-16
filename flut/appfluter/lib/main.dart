import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'dart:convert';
import 'package:firebase_core/firebase_core.dart';
import 'package:firebase_database/firebase_database.dart';
import 'firebase_options.dart';

var FirebaseOptions = FirebaseOptions(
  apiKey: 'AIzaSyBARDg5zparzMVMmn5wmXKf-M9ZR36Ejms',
  appId: '1:856774459322:android:d390f9199d44e03ff5e783',
  messagingSenderId: '856774459322',
  projectId: 'odoodb-afb24',
  storageBucket: 'odoodb-afb24.appspot.com',
);
void main() async {
  WidgetsFlutterBinding.ensureInitialized();

  runApp(MyApp());
  await Firebase.initializeApp(
    options: FirebaseOptions,
  );
}

class MyApp extends StatefulWidget {
  @override
  _MyAppState createState() => _MyAppState();
}

class Myodoo {
  String baseURL;
  String? _url;
  String? _db;
  String? _username;
  String? _password;
  String model = 'product.product';
  String field = 'id,name';
  String search = '';

  /// /web/dataset/
  /// /mail/channel/messages
  ////web/image?model=product.te
  /////return '${this.baseURL}/gateway/product';
  Myodoo(this.baseURL);

  String product() => '$baseURL/gateway/dataset/$model?search=$search';

  String productImage(int id) =>
      '$baseURL/gateway/web/image?model=$model&id=${id.toString()}';
  // http://localhost:8015/gateway/my/image

  String productImageb(int id) {
    return '${this.baseURL}/gateway/web/image?model=${this.model}&id=${id.toString()}';
    // http://localhost:8015/gateway/my/image
  }

  String alamat() {
    return '${this.baseURL}/gateway/image/';
  }

  Future<void> connect() async {
    // TODO: Implement Odoo RPC connection logic
  }

  Future<List<dynamic>> searchProduct(String query) async {
    // TODO: Implement Odoo RPC search product logic
    return [];
  }

  Future<List<dynamic>> getProductImage(int productId) async {
    // TODO: Implement Odoo RPC get product image logic
    return [];
  }
}

class _MyAppState extends State<MyApp> {
  List<dynamic> _data = [];

  final client = Myodoo('http://localhost:8015');
  String _searchTerm = "ped";
  final TextEditingController nameController =
      TextEditingController(text: 'John Doe');

  @override
  void initState() {
    super.initState();
    _fetchData();
    client.model = 'product.product';
  }

  _fetchData() async {
    final response = await http.get(Uri.parse("${client.product()}"));
    if (response.statusCode == 200) {
      setState(() {
        _data = jsonDecode(response.body);
      });
    }
  }

  _search() {
    setState(() {
      _data = _data
          .where((post) =>
              post["title"].toLowerCase().contains(_searchTerm.toLowerCase()))
          .toList();
    });
  }

  bool showAdditionalContent = true;
  @override
  Widget build(BuildContext context) {
    var listView = ListView.builder(
      itemCount: _data.length,
      itemBuilder: (context, index) {
        var image = Image.network(
            width: 100.0,
            'http://localhost:8015/gateway/image/${_data[index]['id']}');

        return ListTile(
          title: Text(_data[index]['name']),
          subtitle: Text(_data[index]['name']),
          leading: image,
        );
      },
    );

    var gridView = GridView.builder(
      gridDelegate: const SliverGridDelegateWithFixedCrossAxisCount(
        crossAxisCount: 2,
      ),
      itemCount: _data.length,
      itemBuilder: (context, index) {
        var image2 = Image.network(
            width: 100.0, client.productImage(_data[index]['id']));
        return Card(
          child: ListTile(
            title: Text(_data[index]["name"]),
            subtitle: Text(_data[index]["name"]),
            leading: image2,
          ),
        );
      },
    );
    var appBar2 = AppBar(
      title: TextField(
          controller: TextEditingController(text: _searchTerm),
          onChanged: (value) {
            _searchTerm = value;
          }
          // Handle the value changed event
          ),
      actions: [
        IconButton(
          icon: Icon(Icons.help),
          onPressed: () {
            // Perform some action
            client.search = _searchTerm;
            _fetchData();
          },
        ),
        IconButton(
          icon: Icon(Icons.search),
          onPressed: () {
            setState(() {
              // Mengubah kondisi saat tombol ditekan
              showAdditionalContent = !showAdditionalContent;
            });
            print(showAdditionalContent);
            // Perform some action
          },
          alignment: Alignment.centerLeft,
        ),
        IconButton(
          icon: Icon(Icons.swap_horiz),
          onPressed: () {
            // Saat IconButton ditekan, ganti body dengan halaman kedua
            setState(() {});
          },
        ),
      ],
    );

    Widget additionalContentWidget = Text(
      'Konten Tambahan',
      style: TextStyle(fontSize: 16),
    );
    Widget bodyWidget() {
      return showAdditionalContent ? gridView : listView;
    }

    return MaterialApp(
      title: "Odoo Product",
      home: Scaffold(
        appBar: appBar2,
        body: bodyWidget(),
      ),
    );
  }
}

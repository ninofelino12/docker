import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'dart:convert';

import 'package:odoo_rpc/odoo_rpc.dart';

void main() {
  runApp(MyApp());
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

  @override
  Widget build(BuildContext context) {
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
            // Perform some action
          },
          alignment: Alignment.centerLeft,
        ),
      ],
    );
    var gridView = GridView.builder(
      gridDelegate: SliverGridDelegateWithFixedCrossAxisCount(
        crossAxisCount: 2,
      ),
      itemCount: _data.length,
      itemBuilder: (context, index) => Card(
        child: ListTile(
          title: Text(_data[index]["name"]),
          subtitle: Text(_data[index]["name"]),
          leading: Image.network(
              width: 100.0, client.productImage(_data[index]['id'])),
        ),
      ),
    );

    return MaterialApp(
      title: "Odoo Product",
      home: Scaffold(
        appBar: appBar2,
        body: gridView,
      ),
    );
  }
}

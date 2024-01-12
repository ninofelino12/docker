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
  String? baseURL;
  String? _url;
  String? _db;
  String? _username;
  String? _password;
  String model = 'product.product';
  String field = 'id,name';

  /// /web/dataset/
  /// /mail/channel/messages
  ////web/image?model=product.te
  Myodoo(this.baseURL);

  String product() {
    //return '${this.baseURL}/gateway/product';
    return '${this.baseURL}/gateway/dataset/${this.model}';
  }

  String productImage(int id) {
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
  String _searchTerm = "http://localhost:8015";
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
    return MaterialApp(
      title: "Flutter App",
      home: Scaffold(
        appBar: AppBar(
          title: TextField(
            controller: nameController,
          ),
        ),
        body: GridView.builder(
          gridDelegate: SliverGridDelegateWithFixedCrossAxisCount(
            crossAxisCount: 2,
          ),
          itemCount: _data.length,
          itemBuilder: (context, index) {
            return Card(
              child: ListTile(
                title: Text(_data[index]["name"]),
                subtitle: Text(_data[index]["name"]),
                leading: Image.network(
                    width: 100.0, client.productImage(_data[index]['id'])),
              ),
            );
          },
        ),
      ),
    );
  }
}

class CustomAppBar extends StatelessWidget implements PreferredSizeWidget {
  @override
  Size get preferredSize => Size.fromHeight(70); // Specify the desired height

  @override
  Widget build(BuildContext context) {
    return AppBar(
      title: Text('_searchTerm'
          // Add TextField properties here
          ),
      actions: [
        PopupMenuButton(
          icon: Icon(Icons.more_vert), // Icon for the menu button
          itemBuilder: (context) => [
            PopupMenuItem(
              value: 1,
              child: Text('Option 1'),
            ),
            PopupMenuItem(
              value: 2,
              child: Text('Option 2'),
            ),
          ],
          onSelected: (value) {
            // Handle menu item selection
          },
        ),
      ],
    );
  }
}

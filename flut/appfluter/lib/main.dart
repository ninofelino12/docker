import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'dart:convert';

void main() => runApp(MyApp());

class MyApp extends StatefulWidget {
  @override
  _MyAppState createState() => _MyAppState();
}

class _MyAppState extends State<MyApp> {
  List<dynamic> data = [];
  List<dynamic> _filteredData = [];
  final TextEditingController _searchController = TextEditingController();

  @override
  void initState() {
    super.initState();
    fetchData();
  }

  Future<void> fetchData() async {
    final response =
        await http.get(Uri.parse('http://localhost:8015/gateway/product'));

    if (response.statusCode == 200) {
      setState(() {
        data = jsonDecode(response.body);
        _filteredData = data; // Initially show all data
      });
    } else {
      // Handle error
    }
  }

  void _searchData() {
    final searchTerm = _searchController.text.toLowerCase();
    _filteredData = data.where((item) {
      final title = item['name'].toString().toLowerCase();
      return title.contains(searchTerm);
    }).toList();
    setState(() {});
  }

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
        appBar: AppBar(),
        body: Column(
          children: [
            TextField(
              controller: _searchController,
              decoration: InputDecoration(
                hintText: 'Search',
                suffixIcon: IconButton(
                  onPressed: _searchData,
                  icon: Icon(Icons.search),
                ),
              ),
            ),
            Expanded(
              child: ListView.builder(
                itemCount: _filteredData.length,
                itemBuilder: (context, index) {
                  return ListTile(
                    title: Text(_filteredData[index]['name']),
                    subtitle: Text(_filteredData[index]['name']),
                    leading: Image.network(
                        'http://localhost:8015/gateway/image/${_filteredData[index]['id']}'),
                  );
                },
              ),
            ),
          ],
        ),
      ),
    );
  }
}

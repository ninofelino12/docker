import 'dart:async';
import 'dart:convert';

import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;

String jsondata = '';

Future<http.Response> fetchPhotos(http.Client client) async {
  return client.get(Uri.parse('https://jsonplaceholder.typicode.com/photos'));
}

void main() => runApp(MyApp());

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Flutter Demo',
      home: MyStatefulWidget(),
    );
  }
}

class MyStatefulWidget extends StatefulWidget {
  @override
  _MyStatefulWidgetState createState() => _MyStatefulWidgetState();
}

class _MyStatefulWidgetState extends State<MyStatefulWidget> {
  int count = 0;

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        backgroundColor: Colors.indigo,
        actions: [
          IconButton(
            icon: Icon(Icons.settings),
            onPressed: () {
              // handle tap
              setState(() {
                print(count++);
              });
            },
          ),
          IconButton(
            icon: Icon(Icons.settings, color: Colors.white),
            onPressed: () {
              // handle tap
              setState(() {
                print(count++);
              });
              // //
              //
              //
              //
            },
          ),
        ],
        title: Text('Stateful Demo', style: TextStyle(color: Colors.white)),
      ),
      body: Center(
        child: Text(
          '$jsondata Count: $count',
          style: TextStyle(fontSize: 20),
        ),
      ),
      floatingActionButton: FloatingActionButton(
        onPressed: () {
          loadJsonFromUrl('http://localhost:8015/gateway/product');

          print("load json");

          setState(() {
            count++;
          });
        },
        child: Icon(Icons.add),
      ),
    );
  }
}

Future<String> loadJsonFromUrl(String url) async {
  final response = await http.get(Uri.parse(url));

  if (response.statusCode == 200) {
    jsondata = response.body;
    final dynamic datajs = jsonDecode(response.body);
    print(datajs['name']);
    // print(jsondata);
    return response.body;
  } else {
    throw Exception('Error loading JSON from URL');
  }
}

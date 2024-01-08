import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'dart:async';
import 'dart:convert';

void main() async {
  runApp(const App());
}

class App extends StatelessWidget {
  const App({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    const title = 'Odoo Controller';
    return MaterialApp(
      title: title,
      home: _buildHome(title),
    );
  }

  Widget _buildHome(String title) {
    return Scaffold(
      appBar: AppBar(
        // ignore: prefer_const_constructors
        title: Text(title),
      ),
      body: Container(),
    );
  }
}

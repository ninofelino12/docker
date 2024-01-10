import 'package:appfluter/json.dart';
import 'package:appfluter/widget/ResponsiveAppBar.dart';
import 'package:appfluter/widget/ResponsiveGridWidget.dart';
import 'package:http/http.dart' as http;
import 'package:flutter/material.dart';
import 'package:appfluter/widget/model.dart';

void main() => runApp(Appb());

void ambildata() {
  loadJsonFromUrl(url).then((value) => {jsondata = value, print(value)});
}

class Appb extends StatelessWidget {
  const Appb({super.key});

  @override
  Widget build(BuildContext context) {
    loadJsonFromUrl(url).then((value) => {jsondata = value, print(value)});
    print(jsondata);
    final items = ["Item 1", "It 2", "It 3", "It 4"];
    return MaterialApp(
        home: Scaffold(
      // body: MyBody(),CustomGridWidget(items: items),
      body: ResponsiveGridWidget(items: items),
      // appBar: CustomAppBar(title: 'Custom Bar'),
      appBar: ResponsiveAppBar(),
    ));
  }
}

class MyBody extends StatelessWidget {
  const MyBody({super.key});

  @override
  Widget build(BuildContext context) {
    return const Placeholder();
  }
}

class MyAp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
        appBar: ResponsiveAppBar(
          onMenuPressed: () {
            // Handle menu icon pressed
          },
        ),
        drawer: Drawer(
          child: ListView(
            padding: EdgeInsets.zero,
            children: [
              DrawerHeader(
                decoration: BoxDecoration(
                  color: Colors.blue,
                ),
                child: Text('Drawer Header'),
              ),
              ListTile(
                title: Text('Menu Item 1'),
                onTap: () {
                  // Handle menu item 1
                  Navigator.pop(context);
                },
              ),
              ListTile(
                title: Text('Menu Item 2'),
                onTap: () {
                  // Handle menu item 2
                  Navigator.pop(context);
                },
              ),
              // Add more menu items as needed
            ],
          ),
        ),
        body: Center(
          child: Text('Hello, World!'),
        ),
      ),
    );
  }
}

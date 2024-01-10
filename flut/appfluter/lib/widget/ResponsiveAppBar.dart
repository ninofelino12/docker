import 'package:flutter/material.dart';
import 'package:connectivity/connectivity.dart';

class ResponsiveAppBar extends StatefulWidget implements PreferredSizeWidget {
  final VoidCallback? onMenuPressed;

  ResponsiveAppBar({this.onMenuPressed});

  @override
  _ResponsiveAppBarState createState() => _ResponsiveAppBarState();

  @override
  Size get preferredSize => Size.fromHeight(kToolbarHeight);
}

class _ResponsiveAppBarState extends State<ResponsiveAppBar> {
  late bool isConnected;
  late ConnectivityResult _connectionStatus;

  @override
  void initState() {
    super.initState();

    Connectivity().onConnectivityChanged.listen((ConnectivityResult result) {
      setState(() {
        _connectionStatus = result;
        isConnected = result != ConnectivityResult.none;
      });
    });

    initConnectivity();
  }

  Future<void> initConnectivity() async {
    ConnectivityResult result;
    try {
      result = await Connectivity().checkConnectivity();
    } catch (e) {
      result = ConnectivityResult.none;
    }

    if (!mounted) {
      return;
    }

    setState(() {
      _connectionStatus = result;
      isConnected = result != ConnectivityResult.none;
    });
  }

  Widget _buildTitle() {
    return LayoutBuilder(
      builder: (context, constraints) {
        if (constraints.maxWidth > 600) {
          return Text(isConnected
              ? 'Connected - Large Screen'
              : 'Offline - Large Screen');
        } else {
          return Text(isConnected
              ? 'Connected - Small Screen'
              : 'Offline - Small Screen');
        }
      },
    );
  }

  @override
  Widget build(BuildContext context) {
    return AppBar(
      title: _buildTitle(),
      actions: [
        IconButton(
          icon: Icon(Icons.search),
          onPressed: () {
            showSearch(context: context, delegate: CustomSearchDelegate());
          },
        ),
      ],
      leading: Builder(
        builder: (context) => IconButton(
          icon: Icon(Icons.menu),
          onPressed: widget.onMenuPressed != null
              ? widget.onMenuPressed
              : () {
                  Scaffold.of(context).openDrawer();
                },
        ),
      ),
    );
  }
}

class CustomSearchDelegate extends SearchDelegate<String> {
  @override
  List<Widget> buildActions(BuildContext context) {
    return [
      IconButton(
        icon: Icon(Icons.clear),
        onPressed: () {
          query = '';
        },
      ),
    ];
  }

  @override
  Widget buildLeading(BuildContext context) {
    return IconButton(
      icon: Icon(Icons.arrow_back),
      onPressed: () {
        close(context, '');
      },
    );
  }

  @override
  Widget buildResults(BuildContext context) {
    // Implement your search results here
    return Container();
  }

  @override
  Widget buildSuggestions(BuildContext context) {
    // Implement your search suggestions here
    return Container();
  }
}

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
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

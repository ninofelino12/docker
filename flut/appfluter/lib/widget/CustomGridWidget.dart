import 'package:flutter/material.dart';

class CustomGridWidget extends StatelessWidget {
  final List<String> items; // Change the type based on your data

  CustomGridWidget({required this.items});

  @override
  Widget build(BuildContext context) {
    return GridView.builder(
      gridDelegate: SliverGridDelegateWithFixedCrossAxisCount(
        crossAxisCount: 4, // Adjust the number of columns as needed
        crossAxisSpacing: 8.0,
        mainAxisSpacing: 8.0,
      ),
      itemCount: items.length,
      itemBuilder: (context, index) {
        return GridItemWidget(item: items[index]);
      },
    );
  }
}

class GridItemWidget extends StatelessWidget {
  final String item; // Change the type based on your data

  GridItemWidget({required this.item});

  @override
  Widget build(BuildContext context) {
    return Container(
      color: Colors.lightBlue, // Customize the color as needed
      child: Center(
        child: Text(
          item,
          style: TextStyle(fontSize: 18.0),
        ),
      ),
    );
  }
}

import 'package:flutter/material.dart';

class ResponsiveGridWidget extends StatelessWidget {
  final List<String> items;

  ResponsiveGridWidget({required this.items});

  @override
  Widget build(BuildContext context) {
    return LayoutBuilder(
      builder: (context, constraints) {
        final double maxWidth = constraints.maxWidth;
        int crossAxisCount = (maxWidth / 200).floor(); // Adjust the item width

        return GridView.builder(
          gridDelegate: SliverGridDelegateWithFixedCrossAxisCount(
            crossAxisCount: crossAxisCount,
            crossAxisSpacing: 8.0,
            mainAxisSpacing: 8.0,
          ),
          itemCount: items.length,
          itemBuilder: (context, index) {
            return GridItemWidget(item: items[index]);
          },
        );
      },
    );
  }
}

class GridItemWidget extends StatelessWidget {
  final String item;

  GridItemWidget({required this.item});

  @override
  Widget build(BuildContext context) {
    return Container(
      color: Colors.lightBlue,
      child: Center(
        child: Text(
          item,
          style: TextStyle(fontSize: 18.0),
        ),
      ),
    );
  }
}

import 'package:flutter/material.dart';

class CustomAppBar extends StatelessWidget implements PreferredSizeWidget {
  final String title;
  final List<Widget>? actions;
  final VoidCallback? onLeadingTap;

  CustomAppBar({
    required this.title,
    this.actions,
    this.onLeadingTap,
  });

  @override
  Widget build(BuildContext context) {
    return AppBar(
      title: Text(title),
      backgroundColor: Colors.blue,
      actions: actions,
      leading: onLeadingTap != null
          ? IconButton(
              icon: Icon(Icons.menu),
              onPressed: onLeadingTap,
            )
          : null,
      // You can customize other properties of the AppBar as needed
      // For example, you can add elevation, background color, etc.
    );
  }

  @override
  Size get preferredSize => Size.fromHeight(kToolbarHeight);
}

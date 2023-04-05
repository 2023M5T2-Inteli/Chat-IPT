import 'package:flutter/material.dart';
import './bottomBar.dart';

class PageContainer extends StatelessWidget {
  const PageContainer(
      {super.key,
      required this.children,
      this.hasBottomBar = false,
      this.hasSettings = false,
      this.center = false});

  final bool hasBottomBar;
  final bool hasSettings;
  final bool center;
  final List<Widget> children;
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      bottomNavigationBar: hasBottomBar
          ? BottomBar(
              hasSettings: hasSettings,
            )
          : null,
      body: Container(
        width: double.infinity,
        decoration: const BoxDecoration(
            image: DecorationImage(
                image: AssetImage("assets/images/background.png"),
                fit: BoxFit.cover)),
        child: Column(
          mainAxisAlignment:
              center ? MainAxisAlignment.center : MainAxisAlignment.start,
          children: children,
        ),
      ),
    );
  }
}

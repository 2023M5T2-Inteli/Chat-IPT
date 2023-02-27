import 'package:flutter/material.dart';

class Button extends StatelessWidget {
  Button(
      {super.key, required this.buttonHandler, required this.text, this.color});
  Function buttonHandler;
  String text;
  MaterialStateProperty<Color?>? color;

  @override
  Widget build(BuildContext context) {
    return ElevatedButton(
      onPressed: () {
        buttonHandler();
      },
      style: ButtonStyle(backgroundColor: color),
      child: Padding(
        padding: EdgeInsets.symmetric(horizontal: 40, vertical: 20),
        child: Text(
          text,
          textAlign: TextAlign.center,
          style: TextStyle(fontSize: 20),
        ),
      ),
    );
  }
}

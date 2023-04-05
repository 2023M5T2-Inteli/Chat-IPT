import 'package:flutter/material.dart';

class Button extends StatelessWidget {
  Button(
      {super.key,
      required this.buttonHandler,
      required this.text,
      this.color,
      this.disabled = false});
  Function buttonHandler;
  String text;
  MaterialStateProperty<Color?>? color;
  bool disabled;

  @override
  Widget build(BuildContext context) {
    return ElevatedButton(
      onPressed: !disabled
          ? () {
              buttonHandler();
            }
          : null,
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

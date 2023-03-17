import 'package:flutter/material.dart';
import '../pages/home.dart';

class TurnOffButton extends StatelessWidget {
  const TurnOffButton({super.key});

  @override
  Widget build(BuildContext context) {
    return Column(
      children: [
        SizedBox(
          height: 60,
        ),
        TextButton(
          onPressed: () {
            Navigator.pushReplacementNamed(
              context,
              '/',
            );
          },
          child: Image(
            image: AssetImage("assets/images/switch.png"),
            fit: BoxFit.cover,
            width: 58,
            height: 58,
          ),
        ),
        SizedBox(
          height: 5,
        ),
        Text(
          "Desligar",
          style: TextStyle(
              color: Colors.white, fontSize: 20, fontWeight: FontWeight.w300),
        ),
        SizedBox(
          height: 20,
        ),
        Divider(
          thickness: 1,
          color: Colors.white,
        ),
        SizedBox(
          height: 30,
        ),
      ],
    );
  }
}

import 'package:flutter/material.dart';
import 'package:flutter/material.dart';

class Cycle extends StatelessWidget {
  const Cycle({super.key, required this.cycle});

  final int cycle;
  @override
  Widget build(BuildContext context) {
    return Column(
      children: [
        SizedBox(
          height: 40,
        ),
        Text(
          "Ciclo",
          style: TextStyle(
              color: Colors.white, fontSize: 14, fontWeight: FontWeight.w400),
        ),
        SizedBox(
          height: 5,
        ),
        Text(
          cycle.toString(),
          style: TextStyle(
              color: Colors.white, fontSize: 50, fontWeight: FontWeight.w400),
        ),
        SizedBox(
          height: 40,
        ),
      ],
    );
  }
}

import 'package:flutter/material.dart';
import 'package:gpt_robot/widgets/components/pageContainer.dart';
import '../components/button.dart';
import '../components/turnOffButton.dart';

class Instructions extends StatelessWidget {
  const Instructions({super.key});

  @override
  Widget build(BuildContext context) {
    return PageContainer(hasBottomBar: true, children: [
      TurnOffButton(),
      Text(
        "Instruções",
        style: TextStyle(
            color: Colors.white, fontSize: 30, fontWeight: FontWeight.w600),
      ),
      SizedBox(
        height: 20,
      ),
      SizedBox(
        width: MediaQuery.of(context).size.width * 0.7,
        child: Text(
          "Organize a bancada da seguinte maneira:",
          textAlign: TextAlign.center,
          style: TextStyle(
              color: Colors.white, fontSize: 20, fontWeight: FontWeight.w400),
        ),
      ),
      SizedBox(
        height: 20,
      ),
      Image(
        image: AssetImage("assets/images/robot_position.png"),
        fit: BoxFit.cover,
        width: MediaQuery.of(context).size.width * 0.8,
        height: MediaQuery.of(context).size.width * 0.8,
      ),
      SizedBox(
        height: 30,
      ),
      Button(
          buttonHandler: () {
            Navigator.pushNamed(context, '/process');
          },
          text: "Iniciar")
    ]);
  }
}

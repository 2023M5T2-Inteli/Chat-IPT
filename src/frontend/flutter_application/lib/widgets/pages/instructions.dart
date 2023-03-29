import 'package:flutter/material.dart';
import '../components/pageContainer.dart';
import '../components/button.dart';
import '../components/turnOffButton.dart';
import '../components/configuration.dart';

class Instructions extends StatefulWidget {
  const Instructions({super.key});

  @override
  State<Instructions> createState() => _InstructionsState();
}

class _InstructionsState extends State<Instructions> {
  void showModal() {
    showModalBottomSheet(context: context, builder: (_) => Configuration());
  }

  @override
  Widget build(BuildContext context) {
    return PageContainer(hasBottomBar: true, hasSettings: true, children: [
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
        height: 40,
      ),
      Button(
          buttonHandler: () {
            showModal();
            // Navigator.pushNamed(context, '/process');
          },
          text: "Configurar")
    ]);
  }
}

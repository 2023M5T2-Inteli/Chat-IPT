import 'package:flutter/material.dart';
import '../components/button.dart';
import '../components/turnOffButton.dart';
import './process.dart';
import './home.dart';

class Instructions extends StatelessWidget {
  const Instructions({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      bottomNavigationBar: Container(
        height: 80,
        decoration: BoxDecoration(
            borderRadius: BorderRadius.circular(30), color: Colors.white),
        child: Row(mainAxisAlignment: MainAxisAlignment.center, children: [
          Transform.translate(
            offset: Offset(0, 0),
            child: TextButton(
              onPressed: () {},
              child: Image(
                image: AssetImage("assets/images/round_logo.png"),
                fit: BoxFit.cover,
                width: 60,
                height: 60,
              ),
            ),
          ),
        ]),
      ),
      body: Container(
        decoration: const BoxDecoration(
            image: DecorationImage(
                image: AssetImage("assets/images/background.png"),
                fit: BoxFit.cover)),
        child: Column(
          children: [
            TurnOffButton(),
            Text(
              "Instruções",
              style: TextStyle(
                  color: Colors.white,
                  fontSize: 30,
                  fontWeight: FontWeight.w600),
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
                    color: Colors.white,
                    fontSize: 20,
                    fontWeight: FontWeight.w400),
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
                  Navigator.push(
                    context,
                    MaterialPageRoute(
                      builder: (ctxt) => Process(),
                    ),
                  );
                },
                text: "Iniciar")
          ],
        ),
      ),
    );
  }
}

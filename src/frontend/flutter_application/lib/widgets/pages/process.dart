import 'package:flutter/material.dart';
import './instructions.dart';
import '../components/button.dart';
import '../components/turnOffButton.dart';

class Process extends StatelessWidget {
  const Process({super.key});

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
              "STATUS",
              style: TextStyle(
                  color: Colors.white,
                  fontSize: 40,
                  fontWeight: FontWeight.w500),
            ),
            SizedBox(
              height: 40,
            ),
            Text(
              "Ciclo",
              style: TextStyle(
                  color: Colors.white,
                  fontSize: 14,
                  fontWeight: FontWeight.w400),
            ),
            SizedBox(
              height: 5,
            ),
            Text(
              "12",
              style: TextStyle(
                  color: Colors.white,
                  fontSize: 50,
                  fontWeight: FontWeight.w400),
            ),
            SizedBox(
              height: 40,
            ),
            SizedBox(
              width: MediaQuery.of(context).size.width * 0.7,
              child: Text(
                "O braço está realizando a separação magnética",
                textAlign: TextAlign.center,
                style: TextStyle(
                    color: Colors.white,
                    fontSize: 20,
                    fontWeight: FontWeight.w400),
              ),
            ),
            SizedBox(
              height: 50,
            ),
            Text(
              "Estágio",
              style: TextStyle(
                  color: Colors.white,
                  fontSize: 14,
                  fontWeight: FontWeight.w400),
            ),
            SizedBox(
              height: 5,
            ),
            Text(
              "3",
              style: TextStyle(
                  color: Colors.white,
                  fontSize: 30,
                  fontWeight: FontWeight.w400),
            ),
            SizedBox(
              width: MediaQuery.of(context).size.width * 0.7,
              child: Row(
                mainAxisAlignment: MainAxisAlignment.spaceBetween,
                children: [
                  IconButton(
                    onPressed: () {},
                    icon: Icon(Icons.arrow_back_ios),
                    color: Colors.white,
                    iconSize: 40,
                  ),
                  IconButton(
                    onPressed: () {},
                    icon: Icon(Icons.stop),
                    iconSize: 40,
                    color: Colors.white,
                  ),
                  IconButton(
                    onPressed: () {},
                    icon: Icon(Icons.arrow_forward_ios),
                    color: Colors.white,
                    iconSize: 40,
                  ),
                ],
              ),
            ),
            SizedBox(
              height: 60,
            ),
            Button(
              buttonHandler: () {
                Navigator.push(
                  context,
                  MaterialPageRoute(builder: (ctxt) => Instructions()),
                );
              },
              text: "Parada de emergência",
              color: MaterialStateProperty.all<Color>(Colors.red),
            )
          ],
        ),
      ),
    );
  }
}

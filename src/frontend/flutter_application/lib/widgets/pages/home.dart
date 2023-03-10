import 'package:flutter/material.dart';
import 'package:gpt_robot/widgets/components/pageContainer.dart';

class Home extends StatelessWidget {
  const Home({super.key});

  @override
  Widget build(BuildContext context) {
    return PageContainer(children: [
      SizedBox(
          height: 300,
          width: 200,
          child: Stack(
            children: const [
              Positioned(
                top: 120,
                child: Text(
                  "GPT",
                  style: TextStyle(
                      fontSize: 70,
                      color: Colors.white,
                      fontWeight: FontWeight.w500),
                ),
              ),
              Positioned(
                top: 190,
                left: 80,
                child: Text(
                  "ROBOT",
                  style: TextStyle(
                      fontSize: 30,
                      color: Colors.white,
                      fontWeight: FontWeight.w500),
                ),
              ),
            ],
          )),
      Image(
        image: AssetImage("assets/images/robot.png"),
        fit: BoxFit.cover,
        width: 350,
        height: 350,
      ),
      SizedBox(
        height: 100,
      ),
      Row(
        mainAxisAlignment: MainAxisAlignment.center,
        children: [
          OutlinedButton(
              style: ButtonStyle(
                  side: MaterialStateProperty.all<BorderSide>(
                      BorderSide(color: Colors.white, width: 2))),
              onPressed: () {
                Navigator.pushNamed(context, '/instructions');
              },
              child: Padding(
                padding:
                    const EdgeInsets.symmetric(vertical: 20, horizontal: 100),
                child: Text(
                  "Ligar",
                  style: TextStyle(color: Colors.white, fontSize: 18),
                ),
              )),
        ],
      )
    ]);
  }
}

import 'package:flutter/material.dart';

class Stage extends StatelessWidget {
  const Stage(
      {super.key,
      required this.isActive,
      required this.decrementStage,
      required this.incrementStage,
      required this.pauseAndPlay,
      required this.stage});

  final bool isActive;
  final int stage;
  final Function decrementStage;
  final Function pauseAndPlay;
  final Function incrementStage;

  @override
  Widget build(BuildContext context) {
    return Column(children: [
      SizedBox(
        height: 50,
      ),
      Text(
        "Estágio",
        style: TextStyle(
            color: Colors.white, fontSize: 14, fontWeight: FontWeight.w400),
      ),
      SizedBox(
        height: 5,
      ),
      Text(
        stage.toString(),
        style: TextStyle(
            color: Colors.white, fontSize: 30, fontWeight: FontWeight.w400),
      ),
      SizedBox(
        width: MediaQuery.of(context).size.width * 0.7,
        child: Row(
          mainAxisAlignment: MainAxisAlignment.spaceBetween,
          children: [
            IconButton(
              onPressed: isActive
                  ? () {
                      decrementStage();
                    }
                  : null,
              icon: Icon(Icons.arrow_back_ios),
              color: Colors.white,
              iconSize: 40,
            ),
            IconButton(
              onPressed: () => pauseAndPlay(),
              icon: isActive ? Icon(Icons.stop) : Icon(Icons.play_arrow),
              iconSize: 40,
              color: Colors.white,
            ),
            IconButton(
              onPressed: isActive
                  ? () {
                      incrementStage();
                    }
                  : null,
              icon: Icon(Icons.arrow_forward_ios),
              color: Colors.white,
              iconSize: 40,
            ),
          ],
        ),
      ),
      SizedBox(
        height: 60,
      )
    ]);
  }
}

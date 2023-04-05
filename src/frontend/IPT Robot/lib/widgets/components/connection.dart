import 'package:flutter/material.dart';
import './pageContainer.dart';

class Connection extends StatelessWidget {
  const Connection({super.key});

  @override
  Widget build(BuildContext context) {
    return PageContainer(center: true, children: [
      SizedBox(
        width: double.infinity,
        height: MediaQuery.of(context).size.height,
        child: Stack(children: [
          Positioned(
            left: 10,
            top: 60,
            child: IconButton(
                onPressed: () {
                  Navigator.pop(context);
                },
                icon: Icon(
                  Icons.arrow_back,
                  color: Colors.white,
                  size: 40,
                )),
          ),
          Center(
            child: CircularProgressIndicator(
              color: Colors.white,
            ),
          )
        ]),
      ),
    ]);
  }
}

import 'package:flutter/material.dart';

class Configuration extends StatelessWidget {
  const Configuration({super.key});

  @override
  Widget build(BuildContext context) {
    return Container(
        height: 600,
        child: Padding(
          padding: EdgeInsets.all(30),
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              Center(
                child: Text(
                  "Configurações",
                  textAlign: TextAlign.center,
                  style: TextStyle(fontSize: 28),
                ),
              ),
              SizedBox(
                height: 15,
              ),
              Divider(
                color: Colors.black,
                thickness: 1,
              ),
              SizedBox(
                height: 30,
              ),
              Text(
                "Força Magnética",
                style: TextStyle(fontSize: 22),
              ),
              SizedBox(
                height: 15,
              ),
              Row(
                mainAxisAlignment: MainAxisAlignment.spaceBetween,
                children: [
                  IconButton(
                    onPressed: () {},
                    icon: Icon(Icons.arrow_back_ios),
                    color: Colors.black,
                    iconSize: 40,
                  ),
                  Text(
                    "1200 Gauss",
                    style: TextStyle(fontSize: 18),
                  ),
                  IconButton(
                    onPressed: () {},
                    icon: Icon(Icons.arrow_forward_ios),
                    color: Colors.black,
                    iconSize: 40,
                  ),
                ],
              )
            ],
          ),
        ));
  }
}

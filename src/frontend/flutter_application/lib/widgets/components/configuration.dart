import 'package:flutter/material.dart';
import './button.dart';

class Configuration extends StatefulWidget {
  const Configuration({
    super.key,
  });

  @override
  State<Configuration> createState() => _ConfigurationState();
}

class _ConfigurationState extends State<Configuration> {
  int cycles = 20;
  int magneticForce = 60000;

  void decrementCycle() {
    if (cycles > 1) {
      setState(() {
        cycles -= 1;
      });
    }
  }

  void incrementCycle() {
    setState(() {
      cycles += 1;
    });
  }

  void decrementMagneticForce() {
    if (magneticForce > 1000) {
      setState(() {
        magneticForce -= 1000;
      });
    }
  }

  void incrementMagneticForce() {
    if (magneticForce < 60000) {
      setState(() {
        magneticForce += 1000;
      });
    }
  }

  @override
  Widget build(BuildContext context) {
    return SizedBox(
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
                "Número de ciclos",
                style: TextStyle(fontSize: 22),
              ),
              SizedBox(
                height: 15,
              ),
              Row(
                mainAxisAlignment: MainAxisAlignment.spaceBetween,
                children: [
                  IconButton(
                    onPressed: () {
                      decrementCycle();
                    },
                    icon: Icon(Icons.arrow_back_ios),
                    color: Colors.black,
                    iconSize: 40,
                  ),
                  Text(
                    cycles.toString(),
                    style: TextStyle(fontSize: 20),
                  ),
                  IconButton(
                    onPressed: () {
                      incrementCycle();
                    },
                    icon: Icon(Icons.arrow_forward_ios),
                    color: Colors.black,
                    iconSize: 40,
                  ),
                ],
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
                    onPressed: () {
                      decrementMagneticForce();
                    },
                    icon: Icon(Icons.arrow_back_ios),
                    color: Colors.black,
                    iconSize: 40,
                  ),
                  Text(
                    "$magneticForce Gauss",
                    style: TextStyle(fontSize: 20),
                  ),
                  IconButton(
                    onPressed: () {
                      incrementMagneticForce();
                    },
                    icon: Icon(Icons.arrow_forward_ios),
                    color: Colors.black,
                    iconSize: 40,
                  ),
                ],
              ),
              SizedBox(
                height: 30,
              ),
              Center(
                child: Button(
                    buttonHandler: () {
                      Navigator.pushNamed(context, '/process', arguments: {
                        'magneticForce': magneticForce,
                        'cycles': cycles
                      });
                    },
                    text: "Iniciar"),
              )
            ],
          ),
        ));
  }
}

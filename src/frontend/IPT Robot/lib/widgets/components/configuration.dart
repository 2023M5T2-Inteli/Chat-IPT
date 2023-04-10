import 'package:flutter/material.dart';
import 'package:shared_preferences/shared_preferences.dart';
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
  String serverIp = '';
  TextEditingController serverIpController = TextEditingController();

  _loadSavedValue() async {
    SharedPreferences prefs = await SharedPreferences.getInstance();
    String savedValue = prefs.getString('serverIpValue') ?? 'p';
    setState(() {
      serverIpController.text = savedValue;
      serverIp = savedValue;
    });
  }

  @override
  void initState() {
    super.initState();
    _loadSavedValue();
  }

  _saveValue(newValue) async {
    SharedPreferences prefs = await SharedPreferences.getInstance();
    await prefs.setString('serverIpValue', newValue);
  }

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
    print(serverIp);
    return SizedBox(
        height: 800,
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
                height: 10,
              ),
              Text(
                "IMPORTANTE:",
                style: TextStyle(
                    fontSize: 18,
                    color: Colors.red,
                    fontWeight: FontWeight.w600),
                textAlign: TextAlign.center,
              ),
              SizedBox(
                height: 10,
              ),
              Text(
                "1- Conecte o computador e o smartphone à rede wifi \"Chat Ipt\".",
                style: TextStyle(fontSize: 18),
              ),
              SizedBox(
                height: 10,
              ),
              Text(
                "2- Coloque o servidor para rodar no computador.",
                style: TextStyle(fontSize: 18),
              ),
              SizedBox(
                height: 10,
              ),
              Text(
                "3- Prencha o endereço IP do servidor que aparece na tela do computador para conseguir se conectar ao braço robôtico.",
                style: TextStyle(fontSize: 18),
              ),
              SizedBox(
                height: 10,
              ),
              Text(
                "IP do servidor",
                style: TextStyle(fontSize: 22),
              ),
              TextField(
                onChanged: (text) {
                  _saveValue(text);
                  setState(() {
                    serverIp = text;
                  });
                },
                controller: serverIpController,
                keyboardType: TextInputType.number,
                decoration: InputDecoration(
                  hintText: 'Digite aqui o IP do servidor...',
                ),
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
                height: 20,
              ),
              Center(
                child: Button(
                    disabled: serverIp == "",
                    buttonHandler: () {
                      Navigator.pushNamed(context, '/process', arguments: {
                        'magneticForce': magneticForce,
                        'cycles': cycles,
                        'serverIp': serverIp
                      });
                    },
                    text: "Iniciar"),
              )
            ],
          ),
        ));
  }
}

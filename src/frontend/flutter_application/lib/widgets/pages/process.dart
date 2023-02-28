import 'package:flutter/material.dart';
import '../components/stage.dart';
import './instructions.dart';
import '../components/button.dart';
import '../components/turnOffButton.dart';
import 'package:socket_io_client/socket_io_client.dart' as IO;

class Process extends StatefulWidget {
  const Process({super.key});

  @override
  State<Process> createState() => _ProcessState();
}

class _ProcessState extends State<Process> {
  late IO.Socket socket;

  @override
  void initState() {
    super.initState();
    initSocket();
  }

  initSocket() {
    print('Tentando se conectar');
    socket = IO.io('http://localhost:3001', <String, dynamic>{
      'autoConnect': false,
      'transports': ['websocket'],
    });
    socket.connect();
    socket.onConnect((_) {
      print('Connection established');
      //  Começando processo de separação
      socket.emit('start_cycle');
    });
    socket.onDisconnect((_) => print('Connection Disconnection'));
    socket.onConnectError((err) => print(err));
    socket.onError((err) => print(err));

    socket.on('stage', (data) {
      print('stage');
      print(data);
      print('--------------');
    });

    socket.on('cycle', (data) {
      print('cycle');
      print(data);
      print('--------------');
    });
  }

  @override
  void dispose() {
    socket.disconnect();
    socket.dispose();
    super.dispose();
  }

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
            Stage(),
            Button(
              buttonHandler: () {
                socket.emit('emergency_stop');
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

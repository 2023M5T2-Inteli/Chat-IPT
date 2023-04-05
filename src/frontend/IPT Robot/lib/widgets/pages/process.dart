// ignore_for_file: prefer_interpolation_to_compose_strings
import 'package:flutter/material.dart';
import '../components/connection.dart';
import '../components/cycle.dart';
import '../components/pageContainer.dart';
import '../components/stage.dart';
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
  int cycle = 1;
  int stage = 1;
  bool isActive = true;
  bool isLoading = false;
  bool isConnected = false;

  void decrementStage() {
    if (cycle == 1 && stage == 1) {
      return;
    }
    setState(() {
      isLoading = true;
    });
    socket.emit("previous_stage");
  }

//   Future<http.Response> fetchAlbum() {
//     return
//   }

  void pauseAndPlay() {
    setState(() {
      isLoading = true;
    });
    if (isActive) {
      socket.emit("stop");
    } else {
      socket.emit("reactivate");
    }
  }

  void incrementStage() {
    setState(() {
      isLoading = true;
    });
    socket.emit("advance_stage");
  }

  @override
  void initState() {
    super.initState();
  }

  initSocket(context) async {
    final arguments = (ModalRoute.of(context)?.settings.arguments ??
        <String, dynamic>{}) as Map;

    print('Tentando se conectar...');
    print('http://' + arguments['serverIp'] + ':3001');
    // http://192.168.197.134:3001
    socket =
        IO.io('http://' + arguments['serverIp'] + ':3001', <String, dynamic>{
      'autoConnect': false,
      'transports': ['websocket'],
    });
    socket.connect();

    socket.on("stage", (data) {
      setState(() {
        stage = data;
      });
    });

    socket.on('cycle', (data) {
      print("cycle");
      print(data);
      setState(() {
        cycle = data;
      });
    });

    socket.on('response_dobot_connect', (data) {
      setState(() {
        isConnected = true;
      });
      //  Começando processo de separação
      socket.emit('start_cycle', arguments);
    });

    socket.onConnect((_) {
      print('Connection established');
      socket.emit("dobot_connect");
    });

    socket.onDisconnect((_) {
      print('Disconnected');
    });
    // socket.onConnectError((err) => print("Erro" err));
    socket.onError((err) => print(err));

    socket.on('response_stop', (data) {
      setState(() {
        isActive = false;
        isLoading = false;
      });
    });

    socket.on('response_reactivate', (data) {
      setState(() {
        isActive = true;
        isLoading = false;
      });
    });

    socket.on("error", (data) {
      print(data);
      Navigator.pop(context);
    });

    socket.on('response_advance_stage', (data) {
      setState(() {
        isLoading = false;
      });
    });

    socket.on('response_previous_stage', (data) {
      setState(() {
        isLoading = false;
      });
    });

    socket.on('response_emergency_stop', (data) {
      Navigator.pop(context);
    });
  }

  @override
  void dispose() {
    print("disposed");
    socket.disconnect();
    socket.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    if (!isConnected) {
      initSocket(context);
      return Connection();
    }
    return PageContainer(
      hasBottomBar: true,
      children: [
        TurnOffButton(),
        Text(
          "STATUS",
          style: TextStyle(
              color: Colors.white, fontSize: 40, fontWeight: FontWeight.w500),
        ),
        Cycle(cycle: cycle),
        SizedBox(
          width: MediaQuery.of(context).size.width * 0.7,
          child: Text(
            "O braço está realizando a separação magnética",
            textAlign: TextAlign.center,
            style: TextStyle(
                color: Colors.white, fontSize: 20, fontWeight: FontWeight.w400),
          ),
        ),
        Stage(
            decrementStage: decrementStage,
            pauseAndPlay: pauseAndPlay,
            incrementStage: incrementStage,
            isActive: isActive,
            isLoading: isLoading,
            stage: stage),
        Button(
          buttonHandler: () {
            socket.emit('emergency_stop');
          },
          text: "Parada de emergência",
          color: MaterialStateProperty.all<Color>(Colors.red),
        )
      ],
    );
  }
}

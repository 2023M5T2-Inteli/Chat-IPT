import 'package:flutter/material.dart';
import 'package:gpt_robot/widgets/pages/instructions.dart';
import 'package:gpt_robot/widgets/pages/process.dart';
import 'widgets/pages/home.dart';
import './utils/materialColor.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'GPT ROBOT',
      theme: ThemeData(
          primarySwatch: createMaterialColor(const Color(0xFF007D95)),
          fontFamily: "Montserrat",
          scaffoldBackgroundColor: Colors.black),
      debugShowCheckedModeBanner: false,
      routes: {
        '/': (context) => Home(),
        '/instructions': (context) => Instructions(),
        '/process': (context) => Process()
      },
    );
  }
}

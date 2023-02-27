import 'package:flutter/material.dart';
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
      home: const MyHomePage(),
      debugShowCheckedModeBanner: false,
    );
  }
}

class MyHomePage extends StatelessWidget {
  const MyHomePage({super.key});

  @override
  Widget build(BuildContext context) {
    return Home();
  }
}

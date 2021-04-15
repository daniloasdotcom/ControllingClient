import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'home.page.dart';

void main() async => {
      WidgetsFlutterBinding.ensureInitialized(),
      await SystemChrome.setPreferredOrientations(
          [DeviceOrientation.portraitUp]), // To turn off landscape mode
      runApp(MyApp())
    };

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Controlling Client',
      debugShowCheckedModeBanner: false,
      theme: ThemeData(
        primarySwatch: Colors.blue,
      ),
      home: Home(),
    );
  }
}


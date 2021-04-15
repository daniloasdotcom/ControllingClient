import 'package:flutter/material.dart';


class Home extends StatefulWidget {
  @override
  _HomeState createState() => _HomeState();
}

class _HomeState extends State<Home> {
  int _people = 0;
  String _infoText = "Pode Entrar";

  void _changePeople(int delta) {
    setState(() {
      _people += delta;

      if(_people < 0){
        _infoText = "Opa!! Contagem negativa não vale";
      } else if (_people <= 49) {
        _infoText = "Pode Entrar!";
      } else {
        _infoText = "Lotado!";
      }
    });
  }

  @override
  Widget build(BuildContext context) {
    return Stack(
      children: <Widget>[
        Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: <Widget>[
            Text("Clientes:$_people",
                style: TextStyle(
                    color: Colors.white, fontWeight: FontWeight.bold, decoration: TextDecoration.none)),
            SizedBox(
              height: 30,
            ),
            Row(
              mainAxisAlignment: MainAxisAlignment.center,
              children: [
                Padding(
                  padding: const EdgeInsets.all(10.0),
                  child: TextButton(
                      onPressed: () {
                        _changePeople(1);
                      },
                      child: Text("+1",
                          style:
                              TextStyle(fontSize: 40.0, color: Colors.white, decoration: TextDecoration.none))),
                ),
                Padding(
                  padding: const EdgeInsets.all(10.0),
                  child: TextButton(
                      onPressed: () {
                        _changePeople(-1);
                      },
                      child: Text("-1",
                          style:
                              TextStyle(fontSize: 40.0, color: Colors.white, decoration: TextDecoration.none))),
                ),
              ],
            ),
            SizedBox(
              height: 30,
            ),
            Text(_infoText,
                style: TextStyle(
                    color: Colors.white,
                    fontStyle: FontStyle.italic,
                    fontSize: 30.0,
                    decoration: TextDecoration.none
                    ),
                    textAlign: TextAlign.center),
          ],
        )
      ],
    );
  }
}
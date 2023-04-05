import 'package:flutter/material.dart';

class BottomBar extends StatefulWidget {
  const BottomBar({
    super.key,
    this.hasSettings = false,
  });

  final bool hasSettings;

  @override
  State<BottomBar> createState() => _BottomBarState();
}

class _BottomBarState extends State<BottomBar> {
//   void showModal() {
//     showModalBottomSheet(
//         context: context,
//         builder: (_) => Configuration(
//               cycles: widget.cycles,
//               magneticForce: widget.magneticForce,
//             ));
//   }

  @override
  Widget build(BuildContext context) {
    List<Widget> items = [
      Text(
        "CHAT IPT",
        textAlign: TextAlign.center,
        style: TextStyle(fontSize: 24, fontWeight: FontWeight.w300),
      ),
    ];

    // if (widget.hasSettings) {
    //   items.add(Positioned(
    //       right: 16,
    //       child: IconButton(
    //           onPressed: () {
    //             showModal();
    //           },
    //           icon: Icon(Icons.settings))));
    // }

    return Container(
        height: 70,
        width: double.infinity,
        decoration: BoxDecoration(
            borderRadius: BorderRadius.circular(30), color: Colors.white),
        child: Stack(alignment: Alignment.center, children: items));
  }
}

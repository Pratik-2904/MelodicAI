import 'package:flutter/material.dart';
import 'package:client/main.dart';

Future<void> showCustomSnackBar(BuildContext context, String message) async {
  await GlobalScaffoldMessenger.scaffoldMessengerKey.currentState
      ?.showSnackBar(
        SnackBar(
          content: Text(message),
          duration: const Duration(seconds: 2),
        ),
      )
      .closed;
}

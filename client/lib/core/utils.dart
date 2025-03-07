import 'package:flutter/material.dart';
import 'package:client/main.dart';

void showSnackBar(BuildContext context, String message) {
GlobalScaffoldMessenger.scaffoldMessengerKey.currentState?.showSnackBar(
SnackBar(content: Text(message)),
);
}

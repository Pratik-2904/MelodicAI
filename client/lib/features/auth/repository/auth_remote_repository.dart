import 'dart:convert';

import 'package:client/core/failure/failure.dart';
import 'package:client/features/auth/model/usermodel.dart';
import 'package:fpdart/fpdart.dart';
import 'package:http/http.dart' as http;

final baseurl = 'http://127.0.0.1:8000';
final authurl = '$baseurl/auth';

class AuthRemoteRepository {
  Future<Either<Failure, Map<String, dynamic>>> login({
    required String email,
    required String password,
  }) async {
    try {
      final response = await http.post(
        Uri.parse('$authurl/login'),
        headers: {'Content-Type': 'application/json'},

        body: jsonEncode({'email': email, 'password': password}),
      );
      if (response.statusCode != 201) {
        //handle the excepetion
        return left(Failure(response.body, response.statusCode.toString()));
      }
      final res = jsonDecode(response.body) as Map<String, dynamic>;
      return right(res);
    } catch (e) {
      return left(Failure(e.toString()));
    }
  }

  Future<Either<Failure, Usermodel>> signup({
    required String name,
    required String email,
    required String password,
  }) async {
    try {
      final res = await http.post(
        Uri.parse('$authurl/signup'),
        headers: {
          'Content-Type': 'application/json',
        }, 
      );
      final user = jsonDecode(res.body) as Map<String, dynamic>;
      
      print(user);

      if (res.statusCode != 201) {
        // {"detail" : Error Message} but i dont want this i want only the error message
        return left(Failure(user['detail'], res.statusCode.toString()));
      }
      
      return right(Usermodel(
        name: user['name'],
        email: user['email'],
        id: user['id'],
      ));

    } catch (e) {
      return left(Failure(e.toString()));
    }
  }

  // Future<Either<Failure, Map<String, dynamic>>> signup({
  //   required String name,
  //   required String email,
  //   required String password,
  // }) async {
  //   try {
  //     final res = await http.post(
  //       Uri.parse('$authurl/signup'),
  //       headers: {
  //         'Content-Type': 'application/json',
  //       }, //this is the header that the server expects suggesting that the body should be in json format but we are sending it in map format we need to send jason format by converting it to the jason
  //       // body: {
  //       //   'name': name,
  //       //   'email': email,
  //       //   'password': password,
  //       // }, //only this without the headers will cause error as the server expects the headers and dictioanry
  //       // //to solve the issue we use jason encode to convert map to dictionary
  //       body: jsonEncode({'name': name, 'email': email, 'password': password}),
  //     );
  //     if (res.statusCode != 201) {
  //       return left(Failure(res.body, res.statusCode.toString()));
  //     }
  //     print(jsonDecode(res.body) as Map<String, dynamic>);
  //     final user = jsonDecode(res.body) as Map<String, dynamic>;
  //     return right(user);

  //   } catch (e) {
  //     return left(Failure(e.toString()));
  //   }
  // }
}

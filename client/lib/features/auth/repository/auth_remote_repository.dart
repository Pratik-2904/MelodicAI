import 'dart:convert';

import 'package:client/core/constants/server_const.dart';
import 'package:client/core/failure/failure.dart';
import 'package:client/features/auth/model/usermodel.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:fpdart/fpdart.dart';
import 'package:http/http.dart' as http;
import 'package:riverpod_annotation/riverpod_annotation.dart';

part 'auth_remote_repository.g.dart';

// final baseurl = 'http://127.0.0.1:8000';
final baseurl = ServerConst.serverbaseUrl;
final authurl = '$baseurl/auth';

@riverpod
AuthRemoteRepository authRemoteRepository(Ref ref) {
  //provider of authRemoteRepository
  return AuthRemoteRepository();
}

class AuthRemoteRepository {
  Future<Either<Failure, Usermodel>> login({
    required String email,
    required String password,
  }) async {
    try {
      final response = await http.post(
        Uri.parse('$authurl/login'),
        headers: {'Content-Type': 'application/json'},
        body: jsonEncode({'email': email, 'password': password}),
      );

      final res = jsonDecode(response.body) as Map<String, dynamic>;
      if (response.statusCode != 200) {
        //handle the excepetion
        // return left(Failure(response.body, response.statusCode.toString()));
        return left(Failure(res['detail'] as String));
      }
      return right(Usermodel.fromMap(res['user']));
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
        headers: {'Content-Type': 'application/json'},
        body: jsonEncode({'name': name, 'email': email, 'password': password}),
      );
      final user = jsonDecode(res.body) as Map<String, dynamic>;

      if (res.statusCode != 201) {
        final errorMessage = user['detail'] is List;
        // {"detail" : Error Message} but i dont want this i want only the error message
        return left(Failure(user['detail'] as String));
      }

      return right(Usermodel.fromJson(res.body));
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

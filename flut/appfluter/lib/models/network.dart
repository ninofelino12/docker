import 'dart:convert';

import 'package:flutter_network_call_base/user.dart';
import 'package:http/http.dart' as http;

const String BASE_URL = "https://reqres.in/api/";

Future<List<User>> getUserList() async {
  final response = await http.get(Uri.parse("${BASE_URL}users?per_page=12"));
  var jsonData = json.decode(response.body);
  return User.parseList(jsonData["data"]);
}

Future<User> getUserDetail(int userId) async {
  final response = await http.get(Uri.parse("${BASE_URL}users/$userId"));
  var jsonData = json.decode(response.body);
  return User.fromJson(jsonData["data"]);
}

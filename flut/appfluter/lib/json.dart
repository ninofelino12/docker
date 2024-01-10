import 'dart:async';
import 'dart:convert';

import 'package:appfluter/widget/model.dart';
import 'package:http/http.dart' as http;

String url = 'http://localhost:8015/gateway/product';

void main() async {
  dynamic decodedData;
  dynamic item;
  String jsonString = '{"name": "John", "age": 30, "city": "New York"}';
  loadJsonFromUrl(url).then((value) => {decodedData = jsonDecode(value)});

  var hasil = await getproduct(decodedData);
  for (item in decodedData) {
    print(item['name']);
  }
  // print(decodedData);
}

Future<dynamic> getproduct(decodedData) async {
  final response = await http.get(Uri.parse(url));
  decodedData = jsonDecode(response.body);
  return decodedData;
}

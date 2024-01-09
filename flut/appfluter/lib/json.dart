import 'dart:async';
import 'dart:convert';

import 'package:appfluter/model.dart';
import 'package:http/http.dart' as http;

String url = 'http://localhost:8015/gateway/product';
void main() {
  loadJsonFromUrl(url).then((value) => {rubah(value)});
  print('hello');
}

rubah(value) {
  var jsondata = jsonDecode(value);
  for (var item in jsondata) {
    print(item['name']);
  }
}

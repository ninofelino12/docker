import 'dart:async';
import 'dart:convert';

import 'package:http/http.dart' as http;

// loadJsonFromUrl(url).then((value) => {rubah(value)});
Future<String> loadJsonFromUrl(String url) async {
  final response = await http.get(Uri.parse(url));

  if (response.statusCode == 200) {
    return response.body;
  } else {
    throw Exception('Failed to load JSON from url');
  }
}

jsonToList(value) {
  var jsondata = jsonDecode(value);
  for (var item in jsondata) {
    print(item['name']);
  }
}

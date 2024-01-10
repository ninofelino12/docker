import 'package:http/http.dart' as http;
import 'dart:convert';

Future<Map<String, dynamic>> fetchJsonFromUrl(String url) async {
  final response = await http.get(Uri.parse(url));

  if (response.statusCode == 200) {
    return jsonDecode(response.body); // Decode the JSON response
  } else {
    throw Exception('Failed to fetch data'); // Handle error
  }
}

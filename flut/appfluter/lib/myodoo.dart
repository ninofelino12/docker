import 'dart:convert';
import 'package:http/http.dart' as http;

Future<void> main() async {
  final sessionId = await authenticate();
  if (sessionId != null) {
    await fetchData(sessionId);
  }
  print(sessionId);
}

Future<String?> authenticate() async {
  print('login');
  final response = await http.post(
    Uri.parse('http://localhost:8015/web/session/authenticate'),
    headers: {'Content-Type': 'application/json'},
    body: jsonEncode({
      'jsonrpc': '2.0',
      'method': 'call',
      'params': {
        'method': 'login',
        'db': 'felino',
        'login': 'ninofelino12@gmail.com',
        'password': 'felino',
      },
      'id': 1,
    }),
  );

  if (response.statusCode == 200) {
    final Map<String, dynamic> data = json.decode(response.body);
    final String? sessionId = data['result']['session_id'];
    return sessionId;
  } else {
    throw Exception('Authentication failed');
  }
}

Future<void> fetchData(String sessionId) async {
  final response = await http.post(
    Uri.parse('http://localhost:8015/web/dataset/call_kw'),
    // 'YOUR_ODOO_SERVER_URL/web/dataset/call_kw',
    headers: {'Content-Type': 'application/json'},
    body: jsonEncode({
      'jsonrpc': '2.0',
      'method': 'call',
      'params': {
        'model': 'res.partner', // Replace with your Odoo model name
        'method': 'search_read',
        'args': [],
        'kwargs': {
          'fields': ['name'],
          'limit': 5
        }, // Specify the fields you want
      },
      'id': 1,
      'session_id': sessionId,
    }),
  );

  if (response.statusCode == 200) {
    final Map<String, dynamic> data = json.decode(response.body);
    final List<dynamic> records = data['result']['records'];
    print(records);
    print('connected');
  } else {
    throw Exception('Failed to load data');
    print('connected');
  }
}

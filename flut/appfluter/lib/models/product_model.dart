import 'dart:async';
import 'dart:convert';
import 'package:http/http.dart' as http;

class Product {
  // Properties (replace placeholders with your actual properties)
  String? name;
  String? description;
  double? price;
  String response = "";
  String hasil = "";
  dynamic? jsondata;
  bool loading = false;
  final String url = 'http://localhost:8015/gateway/product';

  // Constructor
  Product({
    this.name,
    // this.jsondata,

    // this.url,
    // required this.description,
    // required this.price,
    // Add any other required properties here
  });

  // Methods (add methods as needed)
  getcolumn(List<String> field) {
    dynamic item;
    // print(this.response);
    this.jsondata = jsonDecode(this.response);
    for (item in this.jsondata) {
      for (var index = 0; index < field.length; index++) {
        print(item[field[index]]);
        print(field[index]);
      }
    }
  }

  Future<String> loadJsonFromUrl() async {
    this.loading = true;
    final response = await http.get(Uri.parse(url));
    this.loading = false;
    if (response.statusCode == 200) {
      //  print(response.body);
      this.response = response.body;
      this.loading = false;
      //this.jsondata = jsonDecode(this.response)
      return response.body;
    } else {
      this.loading = false;
      throw Exception('Failed to load JSON from url');
    }
  }
}

void main() {
  dynamic decodedData;
  dynamic item;

  var product1 = Product();
  //product1.url = url;
  product1.loadJsonFromUrl().then((value) => {
        product1.getcolumn(['name']),
        product1.getcolumn(['name', 'id']),
        print('eof')
      });
}

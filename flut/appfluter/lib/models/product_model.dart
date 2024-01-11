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
  String baseurl = 'http://localhost:8015/gateway/api';
  // http://localhost:8015/gateway/api?model=res.partner
  String url = 'http://localhost:8015/gateway/product';
  String model = 'res.parner';

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
  setmodel(String model) {
    this.url = '${this.baseurl}?model=${model}';
  }

  list() {
    var hasil = jsonDecode(this.response);
    print("list");
  }

  getcolumn(List<String> field) {
    dynamic item;
    String hasil;
    // print(this.response);
    this.jsondata = jsonDecode(this.response);
    for (item in this.jsondata) {
      hasil = '';
      for (var index = 0; index < field.length; index++) {
        hasil = '${hasil}' + item[field[index]].toString();
      }
      print(hasil);
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

// @http.route('/gateway/api', type='http', auth='none', website=True)
//     def felpartner(self, **kw):
//         # Extract parameters from the request
//         id = int(kw.get('id', 0))
//         ftype = kw.get('type','html')
//         model = kw.get('model', 'res.partner')
void main() {
  // dynamic decodedData;
  // dynamic item;

  var product1 = Product();
  //product1.url = url;
  String nama = "nama";
  String alamat = "alamat";
  print('$nama$alamat');

  product1.setmodel('res.partner');
  print(product1.url);

  product1.loadJsonFromUrl().then((value) => {
        // print(product1.response),
        product1.getcolumn(['id', 'name']),
        //       //  product1.getcolumn(['name', 'id']),
        //       print('eof')
      });
  ;
}

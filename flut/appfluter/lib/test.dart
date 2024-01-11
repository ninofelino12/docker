import 'package:appfluter/models/product_model.dart';

void main() {
  var product1 = Product();

  product1.setmodel('res.partner');

  product1.loadJsonFromUrl().then((value) => {
        // print(product1.response),
        product1.getcolumn(['id', 'name']),
        product1.list(2),
      });
  ;
}

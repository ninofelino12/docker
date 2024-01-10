import 'dart:io';
import 'package:odoo_rpc/odoo_rpc.dart'

main() async {
  final client = OdooClient('https://my-db.odoo.com');
  try {
    await client.authenticate('my-db', 'admin', 'admin');
    final res = await client.callRPC('/web/session/modules', 'call', {});
    print('Installed modules: \n' + res.toString());
  } on OdooException catch (e) {
    print(e);
    client.close();
    exit(-1);
  }
  client.close();
}
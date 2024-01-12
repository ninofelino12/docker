import 'package:odoo/odoo.dart';

final odoo = Odoo(Connection(url: Url(Protocol.http, "localhost", 8069), db: 'odoo'));
UserLoggedIn user = await odoo.connect(Credential("admin", "admin"));
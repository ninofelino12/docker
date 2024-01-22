Example
Initialize the Flask extension:

from flask import Flask
from flask_odoo import Odoo

app = Flask(__name__)
app.config["ODOO_URL"] = "http://localhost:8069"
app.config["ODOO_DB"] = "odoo"
app.config["ODOO_USERNAME"] = "admin"
app.config["ODOO_PASSWORD"] = "admin"
odoo = Odoo(app)
if you are using a Mac you may need to set unverified ssl context

app.config["USE_UNVERIFIED_SSL_CONTEXT"] = "True"
then fetch the Odoo version information by:

>>> odoo.common.version()
{
    "server_version": "13.0",
    "server_version_info": [13, 0, 0, "final", 0],
    "server_serie": "13.0",
    "protocol_version": 1,
}
or call a method on an Odoo model:

>>> odoo["res.partner"].check_access_rights("read", raise_exception=False)
true
If you prefer to use a higher level interface you can declare models by extending odoo.Model as follows:

class Partner(odoo.Model):
    _name = "res.partner"
    _domain = [["active", "=", True]]

    name = odoo.StringType()
count the number of records:

>>> Partner.search_count([["is_company", "=", True]])
1
search and read records:

>>> Partner.search_read([["is_company", "=", True]])
[<Partner(id=1)>]
read records by id:

>>> partner = Partner.search_by_id(1)
>>> partner.name
'Odoo'
create and update records:

>>> new_partner = Partner()
>>> new_partner.name = "Teamgeek"
>>> new_partner.id is None
True
>>> new_partner.create_or_update()
>>> new_partner.id
2
delete records:

>>> existing_partner = Partner()
>>> existing_partner.id = 2
>>> existing_partner.delete()
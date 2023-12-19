from odoo import api, fields, models, SUPERUSER_ID
from odoo.tools.config import config
#config.parse(['--config', 'odoo.conf'])  # Ganti dengan path yang sesuai
from odoo import api, models, registry

db_name = 'feli'
with registry(db_name).cursor() as cr:
    env = api.Environment(cr, SUPERUSER_ID, {})


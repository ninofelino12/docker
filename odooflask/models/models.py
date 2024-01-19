
from odoorpc import fields, models


class gateway(models.Model):
    _name = 'gateway.gateway'
    _description = 'gateway.gateway'

    name = fields.Char()
    value = fields.Integer()
    value2 = fields.Float(compute="_value_pc", store=True)
    description = fields.Text()

    @api.depends('value')
    def _value_pc(self):
        for record in self:
            record.value2 = float(record.value) / 100

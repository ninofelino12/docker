#-*- coding: utf-8 -*-

from odoo import models, fields, api


class iot(models.Model):
    _name = 'iot.iot'
    _description = 'iot.iot'

    name = fields.Char()
    mac = fields.Char()
    board = fields.Char()
    chipb = fields.Char()
    value = fields.Integer()
    value2 = fields.Float(compute="_value_pc", store=True)
    description = fields.Text()
    image = fields.Binary(string='Image')

    @api.depends('value')
    def _value_pc(self):
        for record in self:
            record.value2 = float(record.value) / 100

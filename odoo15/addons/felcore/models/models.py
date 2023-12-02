# -*- coding: utf-8 -*-


from odoo import models, fields, api
import csv

class felcore(models.Model):
    _name = 'felcore.felcore'
    _description = 'felcore.felcore'

    name = fields.Char()
    value = fields.Integer()
    value2 = fields.Float(compute="_value_pc", store=True)
    html_content = fields.Html(string='HTML Content')
    xml_content = fields.Text(string='XML Content')
    description = fields.Text()

    @api.depends('value')
    def _value_pc(self):
        for record in self:
            record.value2 = float(record.value) / 100
   
    def export_data_to_file(self):
        data_to_export = []
        for record in self:
            data_to_export.append({
                 'field1': record.name ,
                 'field2': record.value,
             # Add more fields as needed
            })
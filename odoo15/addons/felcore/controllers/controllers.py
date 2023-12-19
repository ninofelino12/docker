# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request, JsonRequest,json
import json


class Felcore(http.Controller):

    @http.route('/felcore', auth='public', website=True)
    def get_partners(self):
        # uid = request.session.authenticate('felino','ninofelino12@gmail.com','felino')
        # partners = request.env['res.partner'].sudo().search([])
        # partner_data = [{'id': partner.id, 'name': partner.name} for partner in partners]
        return "json.dumps(partner_data)"

    @http.route('/felcore/session',auth='public',website=True)
    def authenticate(self, db, login, password):
        request.session.authinticate('felino','admin','felino')
        return request.env['ir.http'].session_info()

    @http.route('/felcore/modul', auth='public')
    def index(self, **kw):
        return http.request.render('felcore.my_module_template',{})
    @http.route('/felcore/pwa', auth='public')

    def indexpwa(self, **kw):
        return http.request.render('felcore.pwa',{})

    @http.route('/felcore/felcore/objects', auth='public')
    def list(self, **kw):
        return http.request.render('felcore.listing', {
            'root': '/felcore/felcore',
            'objects': http.request.env['felcore.felcore'].search([]),
        })

    @http.route('/felcore/felcore/objects/<model("felcore.felcore"):obj>', auth='public')
    def object(self, obj, **kw):
        return http.request.render('felcore.object', {
            'object': obj
        })

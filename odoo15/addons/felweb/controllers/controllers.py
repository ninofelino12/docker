# -*- coding: utf-8 -*-
from odoo import http


class Felweb(http.Controller):
    @http.route('/felweb/felweb', auth='public')
    def index(self, **kw):
        return http.request.render('felweb.view_partner_qweb', {})

    @http.route('/felweb/felweb/objects', auth='public')
    def list(self, **kw):
        return http.request.render('felweb.listing', {
            'root': '/felweb/felweb',
            'objects': http.request.env['felweb.felweb'].search([]),
        })

    @http.route('/felweb/felweb/objects/<model("felweb.felweb"):obj>', auth='public')
    def object(self, obj, **kw):
        return http.request.render('felweb.object', {
            'object': obj
        })

# -*- coding: utf-8 -*-
from odoo import http


class Felcore(http.Controller):
    @http.route('/felcore', auth='public')
    def index(self, **kw):
        return http.request.render('felcore.web',{})
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

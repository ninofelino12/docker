#-*- coding: utf-8 -*-
from odoo import http


class Iot(http.Controller):
    @http.route('/iot', auth='public')
    def index(self, **kw):
        return http.request.render('iot.mobile',{})

    @http.route('/iot/iot/objects', auth='public')
    def list(self, **kw):
        return http.request.render('iot.listing', {
            'root': '/iot/iot',
            'objects': http.request.env['iot.iot'].search([]),
        })

    @http.route('/iot/iot/objects/<model("iot.iot"):obj>', auth='public')
    def object(self, obj, **kw):
        return http.request.render('iot.object', {
            'object': obj
        })

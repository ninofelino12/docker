# -*- coding: utf-8 -*-
# from odoo import http


# class Gateway(http.Controller):
#     @http.route('/gateway/gateway', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/gateway/gateway/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('gateway.listing', {
#             'root': '/gateway/gateway',
#             'objects': http.request.env['gateway.gateway'].search([]),
#         })

#     @http.route('/gateway/gateway/objects/<model("gateway.gateway"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('gateway.object', {
#             'object': obj
#         })


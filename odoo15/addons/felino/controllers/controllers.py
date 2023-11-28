# -*- coding: utf-8 -*-
import json
from odoo import http
from odoo.http import request


class Felino(http.Controller):
    @http.route('/felino/model', auth='public', methods=['GET'], type='http', csrf=False)
    def get_my_model(self):
        records = request.env['res.partner'].search([])
        # data = [{'name': rec.name} for rec in records]
        return records 
        #request.make_response('data', headers=[('Content-Type', 'application/json')])
    
    @http.route('/felino/felino', auth='public')
    def index(self, **kw):
        return "Hello, worldFel"
    @http.route('/felino/info', auth='public')
    def info(self, **kw):
        records = http.request.env['res.partner'].sudo().search([])
        isi=""
        for rec in records:
            isi=isi+rec.name
        
        return request.make_response("<h1>"+isi)
    @http.route('/felino/product', auth='public')
    def product(self, **kw):
        partners = http.request.env['res.partner'].sudo().search([])
        #partner_list = [{'name': partner.name, 'email': partner.email} 
        partner_list =""
        for partner in partners:
            partner_list="<tr><td>"+partner_list+partner.name+"</td></tr>"
        hasil=json.dumps(partners)
        return request.make_response(hasil)

    @http.route('/felino/felino/objects', auth='public')
    def list(self, **kw):
        return http.request.render('felino.listing', {
            'root': '/felino/felino',
            'objects': http.request.env['res.partner'].search([]),
        })
    @http.route('/felino/coba', auth='public')
    def cobalist(self, **kw):
        print(dir(http.request.env['res.partner'].search([])))
        desktopMenu="menu baru"
        return http.request.render('felino.listing',{'desktopMenu':desktopMenu})
           
        
    
    @http.route('/felino/felino/objects/<model("felino.felino"):obj>', auth='public')
    def object(self, obj, **kw):
        return http.request.render('felino.object', {
            'object': obj
        })

    @http.route('/felino/partners', auth='public', methods=['GET'], cors='*')
    def get_partners(self, **kw):
        partners = request.env['res.partner'].sudo().search([])
        
        partner_list = []
        for partner in partners:
            partner_dict = {
                'id': partner.id,
                'name': partner.name,
                'email': partner.email,
                # tambahkan kolom lainnya sesuai kebutuhan
            }
            partner_list.append(partner_dict)

        response = {
            'status': 'success',
            'partners': partner_list
        }
        return request.make_response(json.dumps(response), headers=[('Content-Type', 'application/json')])


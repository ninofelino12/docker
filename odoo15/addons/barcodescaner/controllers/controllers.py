# -*- coding: utf-8 -*-
from odoo import http

menu_items = [
        {"name": "Home", "url": '//iot/home',"svg":"home.svg"},
        {"name": "Left", "url": '//iot/left',"svg":"left.svg"},
        {"name": "Right", "url": '//iot/right',"svg":"right.svg"},
        {"name": "enter", "url": '//iot/right',"svg":"enter.svg"}]
        # To access the values, you can iterate through the list
hasil=f'<nav class="navbar navbar-dark bg-info navbar-expand d-md-none d-lg-none d-xl-none fixed-bottom"><ul class="navbar-nav nav-justified w-100">'
for item in menu_items:
    hasil=hasil+f"<li class=\"nav-item\"><a class=\"nav-link\" href=\"{item['url']}\" /><span><img src=\"/iot/static/src/img/{item['svg']}\"/></span></a></li>"
hasil=hasil+"<ul></nav>" 

class Barcodescaner(http.Controller):
    @http.route('/barcodescaner', auth='public',website=True)
    def index(self, **kw):
        isi=hasil+"<h2>hello</h2>" 
        return http.request.render('barcodescaner.mobile', {
            'isi': isi
        })
    @http.route('/barcodescaner/landing', auth='public',website=True)
    def landing(self, **kw):
        isi=hasil+"<h2>hello</h2>" 
        return http.request.render('barcodescaner.landing', {
            'isi': isi
        })
    @http.route('/barcodescaner/test', auth='public')
    def indextest(self, **kw):
        isi=hasil+"<h2>hello</h2>" 
        return http.request.render('barcodescaner.mobile', {
            'isi': isi
        })

    @http.route('/barcodescaner/objects', auth='public')
    def list(self, **kw):
        return http.request.render('barcodescaner.listing', {
            'root': '/barcodescaner/barcodescaner',
            'objects': http.request.env['barcodescaner.barcodescaner'].search([]),
        })

    @http.route('/barcodescaner/objects/<model("barcodescaner.barcodescaner"):obj>', auth='public')
    def object(self, obj, **kw):
        return http.request.render('barcodescaner.object', {
            'object': obj
        })

#-*- coding: utf-8 -*-
from odoo import http


class Iot(http.Controller):
    @http.route('/iot', auth='public')
    def index(self, **kw):
        my_string="""
        <h1>IOT</h1>
        Internet of Things (IoT) merujuk pada konsep di mana objek fisik di sekitar kita 
        dilengkapi dengan teknologi dan terhubung ke internet. IoT memungkinkan objek 
        tersebut untuk mengumpulkan dan bertukar data, serta mengambil tindakan berdasarkan 
        data yang dikumpulkan. Ide dasar di balik IoT adalah membuat benda-benda sehari-hari 
        menjadi pintar dan berkomunikasi satu sama lain, membentuk suatu ekosistem yang cerdas dan terhubung.

        """
        return http.request.render('iot.mobile',{'my_string': my_string})
    
    @http.route('/iot/barcode', auth='public')
    def barcode(self, **kw):
        return http.request.render('iot.barcode',{})
    
    @http.route('/iot/menu', auth='public')
    def menu(self, **kw):
        menux=['Home','Left','Right','Enter']
        menu_items = [
        {"name": "Home", "url": '//iot/home',"svg":"home.svg"},
        {"name": "Left", "url": '//iot/left',"svg":"left.svg"},
        {"name": "Right", "url": '//iot/right',"svg":"right.svg"},
        {"name": "enter", "url": '//iot/right',"svg":"enter.svg"}]
        # To access the values, you can iterate through the list
        hasil=f'<nav class="navbar content="width=device-width navbar-light bg-light fixed-bottom"><ul class="navbar-nav nav-justified w-100">'
        for item in menu_items:
            hasil=hasil+f"<li class=\"nav-item\"><a class=\"nav-link\" href=\"{item['url']}\" /><span><img src=\"/iot/static/src/img/{item['svg']}\"/></span></a></li>"
        hasil=hasil+"</ul></nav>" 
        return http.request.render('iot.cetak',{'my_string': hasil})

    @http.route('/iot/objects', auth='public')
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

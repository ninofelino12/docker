#-*- coding: utf-8 -*-
from odoo import http


class Iot(http.Controller):
    @http.route('/iot', auth='public')
    def index(self, **kw):
        my_string="""
        Internet of Things (IoT) merujuk pada konsep di mana objek fisik di sekitar kita dilengkapi dengan teknologi dan terhubung ke internet. IoT memungkinkan objek tersebut untuk mengumpulkan dan bertukar data, serta mengambil tindakan berdasarkan data yang dikumpulkan. Ide dasar di balik IoT adalah membuat benda-benda sehari-hari menjadi pintar dan berkomunikasi satu sama lain, membentuk suatu ekosistem yang cerdas dan terhubung.

        """
        return http.request.render('iot.mobile',{'my_string': my_string})
    
    @http.route('/barcode', auth='public')
    def barcode(self, **kw):
        return http.request.render('iot.barcode',{})

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

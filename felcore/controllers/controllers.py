# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request, JsonRequest,json
import json


class Felcore(http.Controller):
    @http.route('/felinocore', type='http', auth='none' ,website=True)
    def public_page(self):
        print("llllllllllllllllllllllllllllllllllllllll")
        return "http.request.render('your_addon.public_template')"

    @http.route('/felinocore', type='http', auth="public", website=True)
    def web_login(self, redirect=None, **kwargs):
        if request.httprequest.method == 'POST':
            login = kwargs.get('login')
            password = kwargs.get('password')
            database = kwargs.get('database')

            # Perform authentication logic (customize based on your requirements)
            # You may need to establish a connection to the specified database

            # Example: Switch database and check credentials
            with request.env['res.users'].sudo().with_context(dbname=database).pool.cursor() as cr:
                cr.execute("SELECT id FROM res_users WHERE login=%s AND password=%s", (login, password))
                user_id = cr.fetchone()

            if user_id:
                # Login successful
                return http.redirect_with_hash('/web')
            else:
                # Login failed
                return http.request.render('my_login_module.view_login_form', {})

        return http.request.render('view_login_form', {})

   
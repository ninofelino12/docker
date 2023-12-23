import json
import base64
from odoo import http
from odoo.http import request



class Gateway(http.Controller):
    @http.route('/gateway', auth='none')
    def index(self, **kw):
        return request.render('gateway.felino')
    
    @http.route('/gateway/partner',type='http', auth='none',website=True)
    def partner(self, **kw):
        partners = request.env['res.partner'].sudo().search([])
        partner_data = []
        for partner in partners:
            partner_data.append({
                'id': partner.id,
                'name': partner.name,
                'email': partner.email,
                # Add more fields as needed
            })
        json_data = json.dumps(partner_data)
      
        return json_data
    
    @http.route('/gateway/product',type='http', auth='none',website=True)
    def product(self, **kw):
        model='product.product'
        partners = request.env[model].sudo().search([])
        partner_data = []
        for partner in partners:
            partner_data.append({
                'id': partner.id,
                'name': partner.name,
                'detail':partner.description,
                'defaultcode':partner.default_code,

                'dd':partner.detailed_type
                
            })

            # /your_module/query?product_id=123&category_id=456
        response = json.dumps(partner_data)
        # response.headers.add('Access-Control-Allow-Origin', '*')    
        return request.make_response(response, [('Content-Type', 'application/json'),('Access-Control-Allow-Origin', '*')])
    
    @http.route('/gateway/image/<int:product_id>', type='http', auth="none", website=True)
    def product_image(self, product_id, **kwargs):
        product = request.env['product.product'].sudo().browse(product_id)
        image_data = base64.b64decode(product.image_1920)
        return request.make_response(image_data, [('Content-Type', 'image/png')])
    
    @http.route('/gateway/png',type='http', auth='none',website=True)
    def fpng(self, **kw):
        Product = request.env['product.product'].sudo().browse(15)
        product = Product.browse(2) # ganti dengan ID product
        image_1920 = product.image_1920
        print(type(image_1920))
        decoded_data = base64.b64decode(image_1920)        
        # return 'send_file(BytesIO(decoded_data),mimetype='image/png')'
        return "png"
    @http.route('/gateway/model',type='http', auth='none',website=True)
    def fmodel(self, **params):
        product_id = params.get('product_id')
        category_id = params.get('category_id')
        model='ir.model'
        if model=='partner':
           model='res.partner' 
        partners = request.env[model].sudo().search([])
        partner_data = []
        for partner in partners:
            partner_data.append({
                'name': partner.name,
                
            })
        

        return json.dumps(partner_data)    
    @http.route('/gateway/api',type='http', auth='none',website=True)
    def api(self, **kw):
        return request.redirect_query('/web', query=request.params)
        

   

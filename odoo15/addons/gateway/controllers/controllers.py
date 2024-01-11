import json
import base64
from odoo import http
from odoo.http import request
import ast



class Gateway(http.Controller):
    
    
    @http.route('/gateway', auth='none')
    def index(self, **kw):
        return request.render('gateway.felino')
    
    @http.route('/gateway/page', auth='none')
    def indexpage(self, **kwargs):
        database_name = http.request.env.cr.dbname
        return request.render('gateway.fpartner',{'data_to_insert':'Database: '+database_name})
    
    
    @http.route('/gateway/api', type='http', auth='none', website=True)
    def felpartner(self, **kw):
        # Extract parameters from the request
        id = int(kw.get('id', 0))
        ftype = kw.get('type','html')
        model = kw.get('model', 'res.partner')  # Set default model if not provided

        # Define common items for all types
        #common_items = kw.get('items',['id', 'name'])
        items_str = kw.get('items', '[id,name]')
        try:
            common_items = ast.literal_eval(items_str)
        except (ValueError, SyntaxError):
            common_items = ['id','name']

        if not isinstance(common_items, list):
            common_items = ['name','id']

        if ftype == 'img':
            # Image type handling
            if id:
                partner = request.env[model].sudo().browse(id)
                image_data = base64.b64decode(partner.image_1920)
                return request.make_response(image_data, [('Content-Type', 'image/png')])
            else:
                return "no id"
        else:
            # Other types (assuming 'htmlx')
            partners = request.env[model].sudo().search([])

            # Build partner_data using a list comprehension
            partner_data = [
                {item: partner[item] for item in common_items}
                for partner in partners
            ]

            # Convert partner_data to JSON
            response_data = json.dumps(partner_data)

            # Return JSON response with appropriate headers
            return request.make_response(
                response_data, [('Content-Type', 'application/json'), ('Access-Control-Allow-Origin', '*')]
            )
    
    @http.route('/gateway/fapi',type='http', auth='none',website=True)
    def partner(self, **kw):
        id = int(kw.get('id', 0))
        ftype=kw.get('type')
        model=kw.get('model') 
        if not model:
            model='res.partner'

        items=['id','name','function','phone']
        partners = request.env[model].sudo().search([])
        #id=17
        jenis='htmlx'
        if ftype=='img':  
            if id:
                product = request.env[model].sudo().browse(id)
                image_data = base64.b64decode(product.image_1920)
                return request.make_response(image_data, [('Content-Type', 'image/png')])
            else:
                return "no id"  
        else: 
            partner_data = [
            {item: partner[item] for item in items}
            for partner in partners
             ]
            response = json.dumps(partner_data)
            return request.make_response(response, [('Content-Type', 'application/json'),('Access-Control-Allow-Origin', '*')])
        
        
       
    
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
    def fpng(self, **params):
        png_id = int(params.get('id'))
        category_id = params.get('category_id')
        product = request.env['res.partner'].sudo().browse(png_id)
        image_1920 = product.image_1920
        image_data = base64.b64decode(product.image_1920)
        return request.make_response(image_data, [('Content-Type', 'image/png')])
    
    @http.route('/gateway/felino',type='http', auth='none',website=True)
    def felino(self, **params):
        png_id = int(params.get('id'))
        category_id = params.get('category_id')
        jenis = params.get('jenis')
        if jenis == 'png':
            if png_id is None:
                return "none"
            else:
                product = request.env['res.partner'].sudo().browse(png_id)
                image_1920 = product.image_1920
                image_data = base64.b64decode(product.image_1920)
                return request.make_response(image_data, [('Content-Type', 'image/png')])
        else:
            return "loading html files"
        
        

    @http.route('/gateway/model',type='http', auth='none',website=True)
    def femodel(self, **params):
        p_id = params.get('id')
        category_id = params.get('category_id')
        model = params.get('model')
        #return model
        list_of_dict=[{'model':'res.partner'},
                      {'model':'product.product'}]
        
        #model='ir.model'
        try:
            partners = request.env[model].sudo().search([])
            partner_data = []
            for partner in partners:
                partner_data.append({
                    'name': partner.name,
                    'id':partner.id                
                 })
            response=json.dumps(partner_data)    
            return request.make_response(response, [('dcode', model),('Content-Type', 'application/json'),('Access-Control-Allow-Origin', '*')])    
        except Exception as e:
            return f"Error: {e}"

        return json.dumps(partner_data)    
    @http.route('/gateway/api/params',type='http', auth='none',website=True)
    def api(self, **kw):
        return request.redirect_query('/web', query=request.params)

      
            

   

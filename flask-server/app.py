from flask import Flask, request,jsonify,send_file
from flask import render_template
from lib.OdooClient import OdooClient
#import odoo_connect
import xmlrpc.client
import odoorpc
import json
import os
from dotenv import load_dotenv
from flask_restful import Api
from flask_restful import Resource
import base64
import openai
import pickle
from io import BytesIO
app = Flask(__name__)
api = Api(app)
connecting=False
url = 'http://203.194.112.105:80'
db = 'DEMO'
username = 'admin'  
password = 'odooadmin'

odoo = odoorpc.ODOO('localhost', port=8015)
def connect():
    
    port=os.getenv('ODOO_PORT');
    url=os.getenv('ODOO_HOST')
    print(url)
    
    odoo.login('felinosample', 'ninofelino12@gmail.com', 'felino')
    return "connect"

connect()

openai.api_key = "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"
# def opeidef :
#     prompt = "What is the meaning of life?"
#     model = "text-davinci-002"
#     response = openai.Completion.create(engine=model, prompt=prompt, max_tokens=50)
#     answer = response.choices[0].text.strip()
#print(answer)

class ItemResource(Resource):
    def get(self, item_id):
        
        if item_id==0:
            partners = odoo.env['res.partner'].search_read([], ['name', 'email'])
        else:
            partners = odoo.env['res.partner'].search_read([('id','=',item_id)], ['name', 'email'])
        # user = odoo.env.user    
        # user_data = odoo.execute('res.partner', 'read', [user.id])
        response = jsonify(partners)
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
        

    
class Product(Resource):
    def get(self, item_id):
        items =odoo.env['product.product'].search_read([], ['name','barcode','description','image_128'])
        for item in items:
            item['url']="/img/"+str(item['id'])
        response = jsonify(items)
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
        

    


class Img(Resource):
    def get(self, item_id):
        Product = odoo.env['product.product']
        product = Product.browse(item_id) # ganti dengan ID product
        image_1920 = product.image_1920
        print(type(image_1920))
        decoded_data = base64.b64decode(image_1920)        
        return send_file(BytesIO(decoded_data),mimetype='image/png')
        

    def post(self, item_id):
        # Logika untuk menambahkan item baru
        pass

    def put(self, item_id):
        # Logika untuk memperbarui item berdasarkan ID
        pass

    def delete(self, item_id):
        # Logika untuk menghapus item berdasarkan ID
        pass


api.add_resource(ItemResource, '/items/<int:item_id>')
api.add_resource(Product, '/product/<int:item_id>')
api.add_resource(Img, '/img/<int:item_id>')

@app.route('/img')
def indeximg():
    Product = odoo.env['product.product']
    product = Product.browse(17) # ganti dengan ID product
    image_1920 = product.image_1920
    print(type(image_1920))
    decoded_data = base64.b64decode(image_1920)
    # with open('img.png', 'wb') as f:
    #     f.write(decoded_data)
    return send_file(BytesIO(decoded_data),mimetype='image/png')
@app.route('/')
def index():
    return render_template('index.html', title='Home Page')

@app.route('/js')
def indexjs():
    return render_template('odooxml.html', title='Home Page')    

@app.route('/product')
def products():
    return render_template('product.html', title='Home Page')

@app.route('/camera')
def camera():
    return render_template('camera.html', title='camera')

@app.route('/api')
def odpro():
    products=''
    odoo = odoorpc.ODOO('localhost', port=8015)
    odoo.login('felino', 'ninofelino12@gmail.com', 'felino')
    partners = odoo.env['res.partner'].search_read([], ['name', 'email'])
    
    user = odoo.env.user    
    user_data = odoo.execute('res.partner', 'read', [user.id])
    print(partners)
    response = jsonify(partners)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/product_image/<int:product_id>')
def product_image(product_id):
    # Mengambil data gambar dari product.product
    # product = odoo.env['product.product'].browse(product_id)
    product = odoo.env['product.product'].browse(4)
    image_data = product.image_128
    print(image_data)

    product_id = 1
    gambar = odoo.env['product.template'].read(product_id, ['image_128'])
    with open('product_image.png', 'wb') as f:
        f.write(product['image_128'])

    # Mengubah data gambar menjadi base64
    #image_base64 = base64.b64encode(image_data).decode('utf-8')

    # Mengirimkan response dengan header gambar
    # response = Response()
    response = "image_data"
    #response.headers['Content-Type'] = 'image/png'
    # response.data = base64.b64decode(image_base64)
    return response



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0',port=4000)
    #app.run(ssl_context=('server.csr', 'server.key'))
    #app.run(host='0.0.0.0'c,ssl_context=('cert.pem', 'key.pem'))
    #app.run(ssl_context='adhoc',host='0.0.0.0')    
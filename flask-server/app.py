from flask import Flask, request,jsonify,send_file
from flask import render_template
import odoorpc


odoo = odoorpc.ODOO('http://localhost', port=8015)

# Check available databases
print(odoo.db.list())

# Login
odoo.login('db_name', 'user', 'passwd')

# Current user
user = odoo.env.user
print(user.name)            # name of the user connected
print(user.company_id.name) # the name of its company

# Simple 'raw' query
user_data = odoo.execute('res.users', 'read', [user.id])
print(user_data)



#app = Flask(__name__)


def connect():
    
    port=os.getenv('ODOO_PORT');
    url=os.getenv('ODOO_HOST')
    print(url)
    
    odoo.login('felinosample', 'ninofelino12@gmail.com', 'felino')
    return "connect"




@app.route('/api')
def odpro():
   
    return 'response'

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
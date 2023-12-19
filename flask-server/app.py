from flask import Flask, request,jsonify
from flask import render_template
from lib.OdooClient import OdooClient
#import odoo_connect
import xmlrpc.client
import odoorpc
import json

app = Flask(__name__)

menu="""
      <a href="/" class="text-white py-2">Home</a>
      <a href="/odoo" class="text-white py-2">Odoo</a>
      <a href="/iot" class="text-white py-2">Iot</a>
      <a href="/barcode" class="text-white py-2">Barcode</a>
      <a href="/camera" class="text-white py-2">camera</a>
      <a href="/iphone" class="text-white py-2">Iphone camera</a>
      <a href="/viphone" class="text-white py-2">Iphone video</a>
      <a href="/docker" class="text-white py-2">Hosting</a>
      <a href="/qrcode" class="text-white py-2">qrcode</a>



"""
url = 'http://203.194.112.105:80'
db = 'DEMO'
username = 'admin'  
password = 'odooadmin'
odoo_client=OdooClient(url,db, username, password)
models = xmlrpc.client.ServerProxy(f"{url}/xmlrpc/2/object")
odoo = odoorpc.ODOO('localhost', port=8015)


# Login
odoo.login('felino', 'ninofelino12@gmail.com', 'felino')



    
@app.route('/api', methods = ['GET'])
def api():
    name = request.args.get('model', 'Guest')
    if name=='product':
       tabel=odoo_client.product()
    else:   
  # Contoh penggunaan untuk mencari beberapa catatan dari model tertentu
        records = odoo_client.search_records('res.partner',domain=[('is_company', '=', False)],limit=2)
        
    return jsonify(records)


@app.route('/')
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





if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0',port=4000)
    #app.run(ssl_context=('server.csr', 'server.key'))
    #app.run(host='0.0.0.0'c,ssl_context=('cert.pem', 'key.pem'))
    #app.run(ssl_context='adhoc',host='0.0.0.0')    
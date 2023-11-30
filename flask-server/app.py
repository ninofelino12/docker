from flask import Flask, request
from flask import render_template
from lib.OdooClient import OdooClient
#import odoo_connect
import xmlrpc.client

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
db = 'demo-01'
username = 'admin'  
password = 'odooadmin'
odoo_client=OdooClient(url,db, username, password)
models = xmlrpc.client.ServerProxy(f"{url}/xmlrpc/2/object")


def nav(menu_items):
    navclass="navbar navbar-dark bg-info navbar-expand d-md-none d-lg-none d-xl-none fixed-bottom"    
    hasil=f'<nav class="{navclass}"><ul class="navbar-nav nav-justified w-100">'
    for item in menu_items:
        hasil=hasil+f"<li class=\"nav-item\"><a class=\"nav-link\" href=\"{item['url']}\" /><span><img src=\"static/src/img/{item['svg']}\"/></span></a></li>"
    hasil=hasil+"</ul></nav>"
    return hasil
@app.route('/hello')
def hello():
    return render_template('index.html',menu=menu)
@app.route('/')
def menu():
    menu_items = [
        {"name": "Home", "url": '//iot/home',"svg":"home.svg"},
        {"name": "Left", "url": '//iot/left',"svg":"left.svg"},
        {"name": "Right", "url": '//iot/right',"svg":"right.svg"},
        {"name": "enter", "url": '//iot/right',"svg":"enter.svg"}]
    return render_template('bootstrap.html',hasil=nav(menu_items))
        # To access the values, you can iterate through the list
   
@app.route('/barcode')
def barcode():
    return render_template('barcode.html',menu=menu)
@app.route('/qrcode')
def qrcode():
    return render_template('qrcode.html',menu=menu)
@app.route('/iphone')
def iphone():
    return render_template('iphonecamera.html',menu=menu)
@app.route('/viphone')
def viphone():
    return render_template('video-iphone.html',menu=menu)

@app.route('/camera')
def camera():
    return render_template('camera.html',menu=menu)
    

@app.route('/odoo')
def od():
    name = request.args.get('model', 'Guest')
    if name=='product':
       tabel=odoo_client.product()
    else:   
  # Contoh penggunaan untuk mencari beberapa catatan dari model tertentu
        records = odoo_client.search_records('res.partner',domain=[('is_company', '=', False)],limit=100)
        tabel=f'hello,{name}'
        for record in records:
            tabel=tabel+'<tr><td>'+record['name']+"</td></tr>"

    omenu="""    
     <a href="/" class="text-white py-2">Home</a>
      <a href="/odoo?model=product" class="text-white py-2">Product</a>
      <a href="/odoo?model=partner" class="text-white py-2">Partner</a>
      <a href="/odoo?model=kanban" class="text-white py-2">Kanban</a>
      <a href="/odoo?model=odoojs" class="text-white py-2">OdooJs</a>
      <a href="/docker" class="text-white py-2">Hosting</a>
    """  
    return render_template('base.html', logo="/Odoo",title='Home Page'+name,menu=omenu,content='<table>'+tabel+"</table?>")

@app.route('/odoo/product')
def odpro():
    omenu="""    
     <a href="/" class="text-white py-2">Home</a>
      <a href="/odoo" class="text-white py-2">Product</a>
      <a href="/iot" class="text-white py-2">Customer</a>
      <a href="/docker" class="text-white py-2">Hosting</a>
    """  
    tabel=odoo_client.product()
    return render_template('base.html', logo="/Odoo",title='Home Page',menu=omenu,content='<table>'+tabel+"</table?>")


@app.route('/serial')
def serial():
    return render_template('serial.html', title='Home Page',user="felino")
@app.route('/docker')
def docker():
    return render_template('docker.html', title='Home Page',user="felino")
@app.route('/iot')
def iot():
    return render_template('iot.html', title='Home Page',user="felino")
@app.route('/hosting')
def hostinger():
    return render_template('hosting.html', title='Home Page',user="felino")



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0',port=4000)
    #app.run(ssl_context=('server.csr', 'server.key'))
    #app.run(host='0.0.0.0'c,ssl_context=('cert.pem', 'key.pem'))
    #app.run(ssl_context='adhoc',host='0.0.0.0')    
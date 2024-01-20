import base64
from functools import wraps
from flask import Flask, Response, jsonify, render_template_string, request,render_template

#from flask import Flask, jsonify, Response

#from od import Odoofelino
import json
import pandas as pd
from odoorpc.odoo import ODOO
from json2html import *

class Odoofelino(ODOO):
    #server='203.194.112.105'
    userid=0
    odooid=1
    db=[]
    myresponse=''
    model='res.users'
    _databases = None
    _model_data = {}
    field=fields='id,name'.split(',') 
    def __init__(self,model='res.partner', server='203.194.112.105', port=80, database='DEMO',user='odooadmin'):
        self.odoo = ODOO(server, port=port)
        pass
    def logine(self):
        self.odoo.login('DEMO', 'admin', 'odooadmin')
        self.user = self.odoo.env.user
         
    def getfel(self, fields=['name', 'id']):
        model = self.odoo.env[self.model]
        records = model.search([])
        Order = self.odoo.env[self.model]
        order_ids = Order.search([])
        partner_data = []
        records=Order.browse(order_ids)
        return json.dumps([
        {field: getattr(record, field) for field in fields}
        for record in records
    ])
    
    def judulmenu(self):
        with open("static/menu.js", "r") as file:
            script = file.read()
        return script
    def gettemplate(self, id=484):
        arch = self.odoo.env['ir.ui.view'].browse(id).arch
        print(arch)
        return arch
    
    def template(self):
        Order = self.odoo.env['ir.ui.view']
        order_ids = Order.search([])
        hasil='<table>'
        for order in Order.browse(order_ids):
            print(order.name)
            hasil+=f'<tr><td><i class="material-icons">add</i><a href="/report?id={order.id}">{order.name}</a></td></tr>'
        hasil+'</table>'
        
        return hasil
        

    def savefile(self,filename,contents):
        with open('static/'+filename, 'w') as f:
             f.write(contents)


    def getmenu(self,app):
        routes_data = []
        hasil='<nav><ul>'
        link=[]
        combobox=''
        idx=0
        
            
        for rule in app.url_map.iter_rules():
            idx=idx+1
            route_info = {
            "path": rule.rule,
            #"methods": list(rule.methods),
            "endpoint": rule.endpoint
             }
            link.append(rule.rule)
            routes_data.append(route_info)
            if idx>1:
               combobox+=f'<option value="{rule.endpoint}">{rule.rule}</option>'
            hasil+=f'<li> <a id="link{idx}" href="{rule.rule}"><img src="/static/{rule.endpoint}.svg"/>{rule.endpoint.capitalize()}</a></li>'
            print(hasil)
        js=hasil
        self.savefile('combobox.xml',combobox)
        self.savefile('menu.js',js)
        return js


    def gettable(self,fields=['name', 'id']):
        
        self.odoo.login('DEMO', 'admin', 'odooadmin')
        self.getfel()
        model = self.odoo.env[self.model]
        records = model.search([])
        Order = self.odoo.env[self.model]
        order_ids = Order.search([])
        partner_data = []
        records=Order.browse(order_ids)
        print('gettab;')
        hasil=[
        {field: getattr(record, field) for field in fields}
        for record in records
    ] 
        return hasil

    
        
    def db(self):
        #Caching
        if self._databases is None:
            self._databases = self.odoo.db.list()
        return self.odoo.db.list()
    def info(self):
        print('------------------------------------')
        print(self.odoo.db.list(), self.myresponse)
    def image(self,id):
        gambar = self.odoo.env['res.partner'].browse(id)
        print('ambi gamar')
        image_1920 = gambar.image_1920
        image_data = base64.b64decode(gambar.image_1920)
        print('beres')
        return image_data   
    
    def htmlresponse(table_html, status=200):
        response = Response(table_html, status=status, mimetype="text/html")
        response.headers["Access-Control-Allow-Origin"] = "*"
        response.headers["Access-Control-Allow-Methods"] = "GET, POST, PUT, DELETE"
        response.headers["Access-Control-Allow-Headers"] = "Content-Type, Authorization"
        return response
        

  

odoo = Odoofelino(model='res.partner')

app = Flask(__name__)

@app.route("/")
def home(model="product.product", fields='id,name'):
    id = request.args.get("id")
    odoo.getmenu(app)
    model = request.args.get("model")
    odoo.model='res.partner'
    odoo.logine()
    data=odoo.getfel(['id','name'])
    #menu(app)
    hasil=''
    partners = json.loads(data)
    for name in partners:
        print(f"<li>{name}</li>")
        if name['id'] < 25:
            hasil+=f"<ul id='cardt' style='width:25%'>{name['name']}<img style='width:54px' src='/image?id={name['id']}'/></ul>"
    print(hasil)    
    return render_template('app.html',script=odoo.judulmenu(),content=f'<container>{hasil}</container>')

@app.route("/card")
def homecard(model="product.product", fields='id,name'):
    hasil=''
    for number in range(1,5): 
        hasil+=card()
    with open('templates/card.html', 'w') as f:
            f.write(hasil)    
    print('save----------------------------')  
    
    rendered_content = render_template_string('''
    <!DOCTYPE html>
    <html>
    <head>
    <link rel="stylesheet" href="{{ url_for('static', filename='bard.css') }}">                                          
    </head>
    <style>
        container{
          display: flex;
          background-color: blanchedalmond;
        }
      </style>
    <body>
    <container>                                          
    {{ script | safe}}  
    </container>
    {{ content }}  
    </body>
    </html>
    '''
    ,script=hasil,content="isi")
    with open("cardgen.html", "w") as file:
        file.write(rendered_content)
    #template=render_template('appdebug.html',script=odoo.getmenu(app),content=hasil)    
    return render_template('appdebug.html',script='<h1>MENU</h1>',content=hasil)
    #return odoo.htmlresponse(render_template)

def cache_image(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        response = f(*args, **kwargs)
        if response.mimetype.startswith('image/'):
            response.cache_control.max_age = 604800
        return response
    return decorated_function

@app.route("/image")
#@cache_image
def image():
    #id = request.args.get("id")
    id = request.args.get('id')
    model = request.args.get('mode')
    if model:
       modelid=model
    else:
       modelid='res.partner'     
    if id:
       idg=id
    else:
        idg='1'    
    
    odoo.logine()
    gambar=odoo.image(int(idg))
    response = Response(gambar, status=200, mimetype="image/png")   

    return response

@app.route("/table")
def table(model="product.product", fields='id,name'):
    #data=odoo.gettable()
    typefile = request.args.get('type', 'html')
    odoo.logine()
    data=odoo.getfel(['name'])
    table_html = json2html.convert(data)
    response = Response(table_html, status=200, mimetype="text/html")
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Methods"] = "GET, POST, PUT, DELETE"
    response.headers["Access-Control-Allow-Headers"] = "Content-Type, Authorization"
    response.headers["Pragma"] = odoo.fields;
    
    response.headers["X-Custom-Header"] = "value"
    return response
    #return render_template('app.html',script=odoo.judulmenu(),content=table_html)
    
@app.route("/report")
def template(model="ir.actions.report", fields='id,name'):
    #data=odoo.gettable()
    odoo.logine()
    odoo.model='ir.actions.report'
    data=odoo.getfel(['name','model','id'])
    table_html=odoo.gettemplate()
    response = Response(table_html, status=200, mimetype="text/html")
    response_headers = {
    "Access-Control-Allow-Origin": "*",
    "Access-Control-Allow-Methods": "GET, POST, PUT, DELETE",
    "Access-Control-Allow-Headers": "Content-Type, Authorization",
    "Pragma":odoo.fields
     }
   
    return response

@app.route("/template")
def report(model="ir.actions.report", fields='id,name'):
    odoo.logine()
    table_html=odoo.template()
    print(table_html)
    response = Response(table_html, status=200, mimetype="text/html")
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Methods"] = "GET, POST, PUT, DELETE"
    response.headers["Access-Control-Allow-Headers"] = "Content-Type, Authorization"
    response.headers["Pragma"] = odoo.fields;
    return response

@app.route("/addons")
def addons(model="ir.module.module", fields='id,name'):
    #data=odoo.gettable()
    typefile = request.args.get('type', 'html')
    odoo.logine()
    odoo.model='ir.module.module'
    data=odoo.getfel(['name','description','description_html'])
    table_html = json2html.convert(data)
    response = Response(table_html, status=200, mimetype="text/html")
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Methods"] = "GET, POST, PUT, DELETE"
    response.headers["Access-Control-Allow-Headers"] = "Content-Type, Authorization"
    response.headers["Pragma"] = odoo.fields;
    
    response.headers["X-Custom-Header"] = "value"
    #return response
    if typefile=='html':
        return render_template('app.html',content=table_html,name=menu())
    else:
        return response
    
@app.after_request
def add_header(response):
    #response.cache_control.max_age = 604800  # Cache for a week (in seconds)
    print('add header')
    return response


def card():
    card="""
    <ul class="cards">
    <li class="cards__item">
    <div class="card">
      <div class="card__image"><img src="http://127.0.0.1:5000/image/26"></div>
      <div class="card__content">
        <div class="card__title">Flex Basis</div>
        <p class="card__text">This defines the default can be a length (e.g. 20%, 5rem, etc.) or a keyword. The auto keyword means "look at my width or height property."</p>
        <button class="btn btn--block card__btn">Button</button>
      </div>
    </div>
    </li>
    </ul>

    """
    return card
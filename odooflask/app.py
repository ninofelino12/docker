import base64
from functools import wraps
import html
from flask import Flask, Response, jsonify, render_template_string, request,render_template,make_response
import xml.etree.ElementTree as ET


#from flask import Flask, jsonify, Response

#from od import Odoofelino
import json
import pandas as pd
from odoorpc.odoo import ODOO
from json2html import *

class Odoofelino(ODOO):
    """
    Class untuk koneksi ke ODOO
    """
    

    #server='203.194.112.105'
    userid=0
    odooid=1
    db=[]
    myresponse=''
    model='res.users'
    _databases = None
    _model_data = {}
    
    field=fields='id,name'.split(',')
    #user='admin' 
    # password='odooadmin'
    # database='demo'
    port='80'
    # server='203.194.112.105'
    def __init__(self,**kwargs):
        self.server=kwargs.get('server', '203.194.112.105')
        self.port=kwargs.get('port', '80')
        self.database=kwargs.get('database', 'DEMO')
        self.userodoo=kwargs.get('user', 'admin')
        self.password=kwargs.get('password', 'odoadmin')
        self.odoo = ODOO(self.server,port=self.port)
       
        
    def logine(self):
        """
        fungsi login dengan parameter
        user
        password
        database
        """
        #self.odoo.login('DEMO', 'admin', 'odooadmin')
        print('##########################################################')
        print('database',self.database)
        #print(self.user,self.password)
        #self.odoo.login(self.database, self.user,self.password)
        self.odoo.login(self.database,self.userodoo,self.password)
        self.user = self.odoo.env.user
       
        #print(odoo.odoo.report.list())
         
    # def getfel2(self, fields=['name', 'id']):
    #     model = self.odoo.env[self.model]
    #     records = model.search([])
    #     Order = self.odoo.env[self.model]
    #     order_ids = Order.search([])
    #     partner_data = []
    #     records=Order.browse(order_ids)
    #     return json.dumps([
    #     {field: getattr(record, field) for field in fields}
    #     for record in records
    # ])

    def getfel(self, fields=['name', 'id']):
        """Fetches specified fields from records efficiently and returns them as JSON."""

        records = self.odoo.env[self.model].search_read([], fields=fields)  # Single query, read only necessary fields
        return json.dumps([record for record in records])  # Direct serialization

    
    # def getfel31(self, fields=['name', 'id']):
    #     Order = self.odoo.env[self.model]
    #     order_ids = Order.search([])
    #     records=Order.browse(order_ids)
    #     return json.dumps([
    #     {field: getattr(records, field) for field in fields}
    #     for record in records])
        

    def myexecute(self, **kwargs):
        #with self.odoo.work_on(kwargs.get('model', 'product.product')):
        #self.odoo.login(self.database,self.user,self.password)
        self.odoo.login('DEMO', 'admin', 'odooadmin')
        self.user = self.odoo.env.user
        records = self.odoo.env[kwargs.get('model','res.partner')].search_read([], kwargs.get('fields', ['id', 'name']))
        if kwargs.get('type','table') == 'html':
            jsonText=json2html.convert(records)
            response = Response('jsonText', status=200, mimetype="text/json")
        else:    
            jsonText=json.dumps(records)
        response = Response(jsonText, status=200, mimetype="text/json")
        response.headers["Access-Control-Allow-Origin"] = "*"
        response.headers["Access-Control-Allow-Methods"] = "GET, POST, PUT, DELETE"
        response.headers["Access-Control-Allow-Headers"] = "Content-Type, Authorization"
        response.headers["Pragma"] = odoo.fields;
        return response
    
    

    
    def judulmenu(self):
        with open("static/menu.js", "r") as file:
            script = file.read()
        return script
    
    def combobox(self):
        with open("static/combobox.xml", "r") as file:
            script = file.read()
        return script
    def gettemplate(self, id=484):
        self.logine()
        arch = self.odoo.env['ir.ui.view'].browse(id).arch_base
        print(arch)
        root = ET.fromstring(arch)
        html_string = ""
        hasil=''
        for element in root:
            if element.tag == "xpath":
                xpath_expr = element.attrib["expr"]  # Ambil ekspresi XPath
                xpath_element = root.find("xpath")
                fields = xpath_element.findall("field") 
                for field in fields:
                    name = field.attrib["name"]  # Ambil nama field
                    invisible = field.attrib.get("invisible", None)  # Ambil atribut invisible (jika ada)
                    html_string += f'<input type="text" id={name} name="fname"><br><br>'

                
            else:
        # Handle elemen XML lainnya sesuai kebutuhan (jika ada)
                html_string += '<div id={element.tag}>{element.tag}></div>'
        print('uuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuu')    
        print(html_string)
        print('uuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuu') 
        response = Response(html_string, status=200, mimetype="text/html")
        response.headers["Access-Control-Allow-Origin"] = "*"
        response.headers["Access-Control-Allow-Methods"] = "GET, POST, PUT, DELETE"
        response.headers["Access-Control-Allow-Headers"] = "Content-Type, Authorization"
        response.headers["Pragma"] = odoo.fields;
        return response
    
    def template(self):
        Order = self.odoo.env['ir.ui.view']
        order_ids = Order.search([])
        hasil='<table>'
        for order in Order.browse(order_ids):
            print(order.name)
            hasil+=f'<tr><td><i class="material-icons">add</i><a href="/report?id={order.id}">{order.name}</a></td></tr>'
        hasil+'</table>'
        
        return hasil
    def report(self):
        self.logine()
        print(self.odoo.report.list())
        return self.odoo.report.list

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
               #combobox+=f'<option value="{rule.rule}">{rule.endpoint}</option>'
               # <button id="loadButton" onclick="loadJSON('http://127.0.0.1:5000/table','xmlData')">Load XML</button> 
               #combobox+=f'<button id="loadButton" onclick="loadJSON('{rule.endpoint}','xmlData')">{rule.rule}</button>'
               combobox += f'<li><button id="loadButton" onclick="loadJSON(\'{rule.rule}\',\'contents\')">{rule.endpoint}</button></li>'
            hasil+=f'<li> <a id="link{idx}" href="{rule.rule}"><img src="/static/{rule.endpoint}.svg"/>{rule.endpoint.capitalize()}</a></li>'
            #print(hasil)
        js=hasil
        self.savefile('combobox.xml',combobox)
        self.savefile('menu.js',js)
        return js

    def getview(self):
        reports = self.odoo.env['ir.actions.report']
        report_id = reports.search([('name', '=', 'Invoice Report')])
        report = reports.browse(report_id)
        arc_base = report.arc_base
        print(arc_base)
        return arc_base

    def gettable(self,fields=['name', 'id']):
        
        #self.odoo.login('DEMO', 'admin', 'odooadmin')
        self.odoo.login(self.database, self.user,self.password)

        self.user = self.odoo.env.user
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
        

  

#odoo = Odoofelino(model='res.partner')
#odoo = Odoofelino(model='res.partner', server='203.194.112.105', port=80, database='DEMO',user='odooadmin')
odoo = Odoofelino(server='localhost', port=8015, database='felino',user='ninofelino12@gmail.com',password="felino")
print(odoo.info)
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
        #print(f"<li>{name}</li>")
        #if name['id'] < 25:
        hasil+=f"<ul id='cardt' style='width:25%'>{name['name']}<img style='width:54px' src='/image?id={name['id']}'/></ul>"
    #print(hasil)    
    return render_template('app.html',sidebar=odoo.combobox(),script=odoo.judulmenu(),content=f'<container>{hasil}</container>')


def cache_image(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        response = f(*args, **kwargs)
        if response.mimetype.startswith('image/'):
            response.cache_control.max_age = 604800
        return response
    return decorated_function

@app.route("/image")
@cache_image
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
    
@app.route("/template")
def template(model="ir.actions.report", fields='id,name'):
    typeresponse = request.args.get('type','html')
    #reports = odoo.gettemplate()
    odoo.logine()
    #print(odoo.odoo.report.list()['Pricelist'])
    #template = odoo.env['ir.ui.view'].render_template(53, data)
    return 'render_template(template, data)'


   

@app.route("/report")
def report():
    typeresponse = request.args.get('type','html')
    reports = odoo.myexecute(fields=['id','name'],model='ir.actions.report',type=typeresponse)
    return reports

@app.route("/addons")
def addons(model="ir.module.module", fields='id,name'):
    typefile = request.args.get('type', 'html')
    odoo.logine()
    odoo.model='ir.module.module'
    data=odoo.getfel(['name','description','description_html'])
    table_html = json2html.convert(data)
  
    if typefile=='html':
        response = make_response(render_template('app.html',content=table_html))
        response.headers["Pragma"] = odoo.fields;
        return response
        #render_template('app.html',content=table_html)
    
    else:
        return data

@app.route("/addons2")
def addons2(model="ir.module.module", fields='id,name'):
    """Fetches Odoo addon data and returns it as HTML or JSON."""

    typefile = request.args.get('type', 'html')
    odoo.model='ir.module.module'
    # Fetch data efficiently
    data = odoo.getfel(fields=['name', 'description', 'description_html'])

    if typefile == 'html':
        table_html = json2html.convert(data)
        return render_template('app.html', content=table_html), {"Pragma": odoo.fields}  # Set headers directly
    else:
        return jsonify(data)  # Use jsonify for proper JSON responses    

@app.route("/info")
def info():
    """
    info about docstring
    """
    # print(dir(Odoofelino))
    print('------di-------------')
    print(dir(Odoofelino.__dict__))
    print('-------doc--------------')
  
    # print(dir(Odoofelino.__module__))
    # print('---------------------')
    print(dir(Odoofelino))
    print('---------------------')
    balik='<div>'
    hasils= dir(Odoofelino)
    for hasil in hasils:
        if hasil.find('__')<0:
           balik +='<li>'+hasil+'</li>'
    return balik+Odoofelino.__module__

@app.after_request
def add_header(response):
    #response.cache_control.max_age = 604800  # Cache for a week (in seconds)
    #print('add header')
    return response



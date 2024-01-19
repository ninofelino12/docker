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
    db=[]
    myresponse=''
    model='res.users'
    _databases = None
    _model_data = {}
    # odoo = odoorpc.ODOO(server, port=80)
    # user=''
    field=fields='id,name'.split(',') 
    def __init__(self,model='res.partner', server='203.194.112.105', port=80, database='DEMO',user='odooadmin'):
        self.odoo = ODOO(server, port=port)
        #super().__init__()
        #self.login()
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
        

def menu():
    routes_data = []
    hasil='<nav><ul>'
    link=[]
    idx=1
    for rule in app.url_map.iter_rules():
        idx=idx+1
        route_info = {
        "path": rule.rule,
        #"methods": list(rule.methods),
        "endpoint": rule.endpoint
        }
        link.append(rule.rule)
        routes_data.append(route_info)
        hasil+=f'<li> <a id="link{idx}" href="{rule.rule}?type=html"><img src="/static/{rule.endpoint}.svg"/>{rule.endpoint.capitalize()}</a></li>'
        js=f'const menu=`{hasil}`; '
        js=js+f'document.getElementById("menu").innerHTML= "menu" ; '
        with open('static/menu.js', 'w') as f:
            f.write(hasil)
    return hasil    

odoo = Odoofelino(model='res.partner')

app = Flask(__name__)

@app.route("/")
def home(model="product.product", fields='id,name'):
    id = request.args.get("id")
    model = request.args.get("model")
    odoo.logine()
    #data=odoo.getfel(['name'])
    data=app.url_map;
    routes_data = []
    hasil='<nav><ul>'
    link=[]
    idx=1
    for rule in app.url_map.iter_rules():
        idx=idx+1
        route_info = {
        "path": rule.rule,
        #"methods": list(rule.methods),
        "endpoint": rule.endpoint
        }
        link.append(rule.rule)
        routes_data.append(route_info)
        hasil+=f'<li> <a id="link{idx}" href="{rule.rule}"><img src="/static/{rule.endpoint}.svg"/>{rule.endpoint.capitalize()}</a></li>'
    json_string = json.dumps(link)
    print(link)
    hasil+='</ul></nav>'
    print(hasil)
    with open('templates/app.html', 'r') as f:
         content = f.read()
    rendered_content = render_template_string(content,name=hasil)
    with open('rendered_page.html', 'w') as f:
        f.write(rendered_content)
    with open("static/menu.js", "r") as file:
        script = file.read()
    return render_template('app.html',name=hasil,script=script)

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
    #return response
    if typefile=='html':
        return render_template('app.html',script=odoo.judulmenu(),content=table_html)
    else:
        return response

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

import base64
import json
from flask import Flask, jsonify,render_template,make_response, request
from flask_odoo import Odoo
import yaml

app = Flask(__name__)
app.config["ODOO_URL"] = "http://localhost:8015"
app.config["ODOO_DB"] = "felino"
app.config["ODOO_USERNAME"] = "ninofelino12@gmail.com"
app.config["ODOO_PASSWORD"] = "felino"
odoo = Odoo(app)
#config = app.config.from_yaml("app.yaml")



def generate_html(partners):
    xml_data = '<?xml version="1.0" encoding="UTF-8" ?>\n<partners>\n'
    for partner in partners:
        xml_data += f'    <id>http:/{partner["name"]}/{partner["id"]}</id>\n'
    return xml_data

def list_methods():
    methods = []
    html=''
    for rule in app.url_map.iter_rules():
        methods.append({
            'endpoint': rule.endpoint,
            'methods': ', '.join(rule.methods)
        })
        html+=f'<li>{rule.endpoint}</li>'
    return html        
    #return jsonify(methods)

  
    


@app.route("/link")
def link():
    modelid = request.args.get("model",'res.partner')
    domain = [('name', 'ilike', 'ab')]

    
    if request.args.get("field"):
       print('ada field');
       fields=request.args.get("field").split(',') 
    else:   
        fields = ['id', 'name']

    # customers = odoo[modelid]
    partners   = odoo[modelid].search_read([],fields)
    print('---------------------------------------')
    print(modelid)
    formatted_partners = [{'id': f'http:/name/{partner["id"]}', 'name': partner['name']} for partner in partners]
    #return {'partners': partners} 
    headers = {"Content-Type": "application/json", "Pragma": "My Value"}
    response = make_response(jsonify(formatted_partners))
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Methods"] = "GET, POST, OPTIONS"
    response.headers["Access-Control-Allow-Headers"] = "Content-Type, Authorization"
    response.headers["Content-Type"] = "application/json";
    return response

@app.route('/sidebar')
def sidebar(**kwargs): 
    menu=[
            {"name":"Partner","url":"link"},
            {"name":"Product","url":"http://127.0.0.1:5000/datasheet?model=product.product&field=name,description"},
            {"name":"Report","url":"localhos:5000/link?model=product.product"}
        ]
    with open('model.yaml', "r") as f:
        data = yaml.load(f, Loader=yaml.FullLoader)
    response = make_response(jsonify(menu))    
    response = make_response(jsonify(data))
    response.headers["Access-Control-Allow-Origin"] = "*"
    return response

@app.route('/')
def index():
    script="""
    <script>
    
    </script>
    """
    html=script
    host = request.host
    print(f'Request :{host}')
    with open('model.yaml', "r") as f:
         datas = yaml.load(f, Loader=yaml.FullLoader)
    for data in datas:
        print(datas[data]['model'])
        model=datas[data]['model']
        field=datas[data]['field']
        #url=f'"dataset/{model}"'
        url=f"'http://127.0.0.1:5000/dataset/{model}'"
        print(url)
        #html+=f'<li><a href="/dataset/{model}?field={field}" onclick="alert("click")" >{datas[data]["name"]}</a></li>' 
        html+=f'<md-filled-button onclick="loadJson2('+url+f')" >{datas[data]["name"]}</md-filled-button>' 
    html+=''
    return render_template("index.html",sidebar=html,main='ssss',script=script) 
    
@app.route('/delete_customer')
def delete_customer():
    # Delete a customer from Odoo.
    odoo.execute('res.partner', 'unlink', [1])

    return 'Customer deleted successfully.'

# def update_name(item):
#     if "name" in item:
#         item["name"] = f"http://localhost/{item['id']}"
#     return item

@app.route("/datasheet")
def datasheet():
    modelid = request.args.get("model",'res.partner')
    domain = [('name', 'ilike', 'ab')]
    if request.args.get("field"):
       fields=request.args.get("field").split(',') 
    else:   
        fields = ['id', 'name']
    partners   = odoo[modelid].search_read([],fields)
    if request.args.get("display"):
       partners= list(map(lambda item: {**item, "image_128": f"http://localhost/image/{item['id']}"}, partners))
    
    if request.args.get("type"):
       return {'partners': partners}    
    
    headers = {"Content-Type": "application/json", "Pragma": "My Value"}
    response = make_response(jsonify(partners))
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Methods"] = "GET, POST, OPTIONS"
    response.headers["Access-Control-Allow-Headers"] = "Content-Type, Authorization"
    response.headers["Content-Type"] = "application/json";
    #list(map(lambda item: {"name": item["name"]}, data))
    #result = list(map(lambda item: {**item, "name": "http://localhost/"}, data))
    return response
#data=datasheet(model='res.partner',field='id,name',type='json')
    #print(type(data)) 

with open('model.yaml', "r") as f:
        data = yaml.load(f, Loader=yaml.FullLoader)

@app.route("/dataset/<models>")
def partner(models):
    partners   = odoo[data[models]['model'] ].search_read([],data[models]['field'].split(','))
    header={"Access-Control-Allow-Origin": "*", "Access-Control-Allow-Methods": "GET, POST, OPTIONS", "Access-Control-Allow-Headers": "Content-Type, Authorization"}
    #header["Content-Type"]="text/html"
    #response = make_response({'partners': partners}, 200, header)
    
    hasil=json_string = json.dumps(partners, default=lambda x: x.__dict__)
    response = make_response(hasil, 200, header)
    return response

@app.route("/image")
def images():
    if request.args.get("id"):
       print('ada field');
       idgbr = request.args.get("id")
    else:   
        idgbr='16'

    partners   = odoo['product.product'].search_read([['id','=',idgbr]],["image_128"])
    gbr=partners[0]
    #data = json.loads(gbr)
    gambar=gbr.get('image_128')
    image_data = base64.b64decode(gambar)
    response = make_response(image_data)
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Methods"] = "GET, POST, OPTIONS"
    response.headers["Access-Control-Allow-Headers"] = "Content-Type, Authorization"
    response.headers["Content-Type"] = "image/png";
    return response

@app.route("/product")
def product():
    partners   = odoo['product.product'].search_read([],['id','name'])
    hasil='<html>'
    nama=''
    style='style="width:50px"'
    url=''
    for partner in partners:
        print(partner)
        name=partner.get('name')
        url=f'<img {style} src="http://localhost:5000/image?id={partner.get("id")}">'
        hasil+=f'<div class="card">{url}<div class"container"><h1>{name}</h1>2</div></div>'
    headers = {"Content-Type": "text/html", "Pragma": "My Value"}
    response = make_response(hasil+'</html>')
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Methods"] = "GET, POST, OPTIONS"
    response.headers["Access-Control-Allow-Headers"] = "Content-Type, Authorization"
    partner_fields = odoo['res.partner'].fields_get()
    for field_name, field_data in partner_fields.items():
            field_type = field_data['type']
            field_label = field_data['string']

            # Do something with the field type and label, e.g., print them:
            print(f"Field Name: {field_name}, Type: {field_type}, Label: {field_label}")
    return render_template('product.html',content=hasil)



if __name__ == '__main__':
    app.run()

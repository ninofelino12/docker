import base64
import json
from flask import Flask, jsonify,render_template,make_response, request
# from flask_odoo import Odoo
from odoorpc.odoo import ODOO
import yaml
# import logging
# import pickle

app = Flask(__name__)
app.config["ODOO_URL"] = "http://localhost:8015"
app.config["ODOO_DB"] = "felino"
app.config["ODOO_USERNAME"] = "ninofelino12@gmail.com"
app.config["ODOO_PASSWORD"] = "felino"
# odoo = Odoo(app)
# fel=ODOO('localhost',port=8015)
# logging.basicConfig(
#     format="%(asctime)s %(levelname)-8s %(message)s",
#     level=logging.INFO,
#     filename="my_log.txt",
# )
# Material(app)

#config = app.config.from_yaml("app.yaml")

class felino():
    def __init__(self, name):
        self.name = name

    def generate_html(partners):
        xml_data = '<?xml version="1.0" encoding="UTF-8" ?>\n<partners>\n'
        for partner in partners:
            xml_data += f'    <id>http:/{partner["name"]}/{partner["id"]}</id>\n'
        return xml_data

my_object = felino("nino")
# with open("class.pickle", "wb") as file:
#     pickle.dump(my_object, file)

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
    # flash   
    hasil=jsonify(data)    
    hasil = map(lambda item: {item[0]}, data.items())
    response = make_response(jsonify(hasil))
    
    print("List of keys:")
    
    response.headers["Access-Control-Allow-Origin"] = "*"
    return data

@app.route('/')
def index():
    script="""
    <script>
    
    </script>
    """
    html=''
    host = request.host
    side=''
    print(f'Request :{host}')
    with open('model.yaml', "r") as f:
         datas = yaml.load(f, Loader=yaml.FullLoader)
    for data in datas:
        print(datas[data]['model'])
        model=datas[data]['model']
        field=datas[data]['field']
        #url=f'"dataset/{model}"'
        url=f"'http://127.0.0.1:5000/dataset/{model}'"
        url2=f"'http://127.0.0.1:5000/report/{model}'"
        print(field)
        print(url)
        parameter=",'hasil','table'"
        parameter2=",'hasil','card'"
        #html+=f'<li><a href="/dataset/{model}?field={field}" onclick="alert("click")" >{datas[data]["name"]}</a></li>' 
        html+=f'<md-filled-button onclick="ambilData('+url+f'{parameter})" >{datas[data]["name"]}</md-filled-button>'
        side+=f'<md-filled-button onclick="ambilData('+url2+f'{parameter2})" >{datas[data]["name"]}</md-filled-button>' 
    html+=''
    rendered_content =render_template("flask.html",side=side,sidebar=html,main='ssss',script=script)
    with open('output.html', 'w') as f:
        f.write(rendered_content)
    return  rendered_content
    
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
    #modelid = request.args.get("model",'res.partner')
    modelid = request.args.get("model",'ir.act.report')
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

def has_key(item,key):
    """
    Checks if the given dictionary has the specified key.

    Args:
        item: The dictionary to check.
        key: The key to check for.

    Returns:
        True if the key exists, False otherwise.
    """
    return key in item
def ubah_key(item,model):
    if has_key(item,'avatar_128'):
        item['avatar_128']=f'<img src="image?id={item["id"]}&model={model}"/>attach'
    if has_key(item,'image_128'):
        item['image_128']=f'<img src="image?id={item["id"]}&model={model}"/>attach'     
    return item


@app.route("/dataset/<models>")
def partner(models):
    print('-----------------------------------')
    print(models)
    print(data[models]['model'])
    print(data[models]['field'])
    partners   = odoo[data[models]['model'] ].search_read([],data[models]['field'].split(','))
    header={"Access-Control-Allow-Origin": "*", "Access-Control-Allow-Methods": "GET, POST, OPTIONS", "Access-Control-Allow-Headers": "Content-Type, Authorization"}
    excluded_fields = ['image', 'document']
    
    #data_baru=list(map(ubah_key, partners))
    data_baru = list(map(lambda item: ubah_key(item,data[models]['model']), partners))

    print(json.dumps(data_baru))
    #hasil=json_string = json.dumps(partners, default=lambda x: x.__dict__)
    hasil=json_string = json.dumps(data_baru, default=lambda x: x.__dict__)

    response = make_response(hasil, 200, header)
    return response

@app.route("/image2")
def images():
    if request.args.get("id"):
       print('ada field');
       idgbr = request.args.get("id")
    else:   
        idgbr='16'
    if request.args.get("model"):
       model=request.args.get("model")
    else:
        model=request.args.get("res.partner")

    partners   = odoo[model].search_read([['id','=',idgbr]],["image_128"])
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

@app.route("/image")
def images2():
    idgbr = request.args.get("id", "16")  # Get "id" from query string, default to "16"
    model = request.args.get("model", "res.partner")  # Get "id" from query string, default to "16"
    image = request.args.get("image", "image_128")  # Get "id" from query string, default to "16"
        
    partners = odoo[model].search_read([['id', '=', idgbr]], [image])
    gbr = partners[0]
    gambar = gbr.get(image)

    if gambar:  # Check if image data exists
        image_data = base64.b64decode(gambar)
        response = make_response(image_data)
        response.headers.update({
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Methods": "GET, POST, OPTIONS",
            "Access-Control-Allow-Headers": "Content-Type, Authorization",
            "Content-Type": "image/png",
        })
        return response
    else:
        return "Image not found", 404  # Return a 404 error if image not found

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



@app.route("/report/<models>")
def report2(models):
    field= ['name']
    field=data[models]['field'].split(',')
    print(models)
    #print(data[models]['field'])
    # fel=ODOO('localhost',port=8015)
    
    fel.login(app.config["ODOO_DB"],app.config["ODOO_USERNAME"],app.config["ODOO_PASSWORD"])
  
    #record=fel.env[data[models]['model']].search([])
    record=fel.env[data[models]['model']].search([])
    
    hasil=fel.execute(data[models]['model'], 'read',record,field)
    return json.dumps(hasil)

@app.route("/report2/<models>")
def report3(models):
    fel = ODOO('localhost', port=8015)
    fel.login(app.config["ODOO_DB"], app.config["ODOO_USERNAME"], app.config["ODOO_PASSWORD"])
    Order = fel.env['ir.ui.view']
    reports = Order.search([])
    # Return JSON directly using list comprehension:
    return json.dumps([{"id": order.id, "name": order.name} for order in reports])

    
if __name__ == '__main__':
    app.run()

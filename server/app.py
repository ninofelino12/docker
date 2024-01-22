from flask import Flask, jsonify,render_template,make_response, request
from flask_odoo import Odoo

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
            {"name":"Product","url":""},
            {"name":"Product","url":"localhos:5000/link?model=product.product"}
        ]
   
    response = make_response(jsonify(menu))
    response.headers["Access-Control-Allow-Origin"] = "*"
    return response

@app.route('/')
def index():
    sidebar="""
    <div >
  
   
   
    <div>
    
    
    """
    return render_template("index.html",sidebar=sidebar,main='ssss') 
    
@app.route('/delete_customer')
def delete_customer():
    # Delete a customer from Odoo.
    odoo.execute('res.partner', 'unlink', [1])

    return 'Customer deleted successfully.'

if __name__ == '__main__':
    app.run()

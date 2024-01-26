from flask import Flask,jsonify,send_file,render_template
import yaml
import logging
import pickle
from odoorpc import ODOO
import base64

from odooclient import OdooClient


 
app = Flask(__name__)

@app.route("/")

def hello_world():
    myodo=OdooClient("localhost","8015",'felino','ninofelino12@gmail.com','felino')
    data = {
        'title': 'My Flask App',
        'greeting': 'Hello, Flask!',
        'content': 'Welcome to my Flask web application.'
    }
    user = myodo.env.user
    print(dir(user))
    print(user.name)            # name of the user connected
    print(user.company_id.name) # the name of its company
    print(user.massage_unread)
    print(dir(user.massage_unread))
    #return jsonify(myodo.f_execute('product.product','html'))
    heade=f'<h1>{user.company_id.name}</h1><h3>{user.email}{user.phone}<address>{user.street}</address></h3>'
    nav=myodo.nav()
    return render_template('index.html',header=heade,nav=nav)

@app.route("/image")

def images():
    myodo=OdooClient("localhost","8015",'felino','ninofelino12@gmail.com','felino')
    image_stream=myodo.f_execute('res.partner','jpg')
    #return jsonify()
    print(image_stream)
    with open('\image\avatar_image.png', 'wb') as image_file:
        image_file.write(image_stream)
    return send_file('\image\avatar_image.png', mimetype='image/png')

@app.route("/view")

def view():
    myodo=OdooClient("localhost","8015",'felino','ninofelino12@gmail.com','felino')
    image_stream=myodo.f_execute('ir.ui.view','xml')
    #return jsonify()
    print(image_stream)
    
    return image_stream


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
        item['avatar_128']=f'<img src="image?id={item["id"]}&model={model}"/>'
    if has_key(item,'image_128'):
        item['image_128']=f'<img src="image?id={item["id"]}&model={model}"/>'     
    if has_key(item,'arch_base'):
        item['arch_base']=f'<a href="view?id={item["id"]}&model={model}"/>{item["name"]}</a>'       
    return item

@app.route("/model/<model>")

def model(model):
    myodo=OdooClient("localhost","8015",'felino','ninofelino12@gmail.com','felino')
    hasil=myodo.f_execute(model,'html') 
    print(hasil)
    data_baru = list(map(lambda item: ubah_key(item,model),hasil))

    # hasil=json_string = json.dumps(data_baru, default=lambda x: x.__dict__)
    return jsonify(hasil)
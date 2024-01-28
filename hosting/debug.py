# import odoorpc
import yaml
import logging
import pickle
from odoorpc import ODOO
import base64
import xmltodict
from sqlalchemy import create_engine, inspect
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float, Boolean  # Import common data types


from odooclient import OdooClient

def extract_buttons(data):
    buttons = []
    
    if isinstance(data, dict):
        if 'button' in data:
            buttons.extend(data['button'])
        
        for key, value in data.items():
            buttons.extend(extract_buttons(value))
    
    elif isinstance(data, list):
        for item in data:
            buttons.extend(extract_buttons(item))
    
    return buttons


server = 'localhost'
port = '8015'
dbname = 'felino'
user = 'ninofelino12@gmail.com'
password = 'felino'


serialized_object = pickle.dumps(OdooClient)
with open('felino.class', 'wb') as file:
    file.write(serialized_object)


loaded_obj = pickle.loads(serialized_object)
# loaded_obj.save()   

myodo=OdooClient("localhost","8015",'felino','ninofelino12@gmail.com','felino')
# serialized_object = pickle.dumps(myodo)
with open('odoo.class', 'wb') as file:
    file.write(serialized_object)




hasil=loaded_obj("localhost","8015",'felino','ninofelino12@gmail.com','felino')
client=hasil.f_execute('product.product','json')
myodo=OdooClient("localhost","8015",'felino','ninofelino12@gmail.com','felino')
myodo.setmodel('product.template',['id','name'],[],'image128')
#print(myodo.getmodel())

myodo.setmodel('res.partner',['id','name'],[],'avatar')
#print(myodo.getmodel())
#----------------- get report
id=4
report=myodo.execute('ir.ui.view', 'read',id,['arch_base'])
#print(report[0]['arch_base'])
#print(myodo.getAttachment())
hasil=report[0]['arch_base']
my_dict=xmltodict.parse(hasil)
#dict=dict['form']
print(my_dict.keys())
print('------------------------- HTML ')
def generate_html(my_dict):
    html = ""
    for key, value in my_dict.items():
        html += f"<{key}>"
        if isinstance(value, dict):
            for subkey, subvalue in value.items():
                html += f"<{subkey}>"
                if subvalue:
                    #html += f"<{subkey}>{''.join(str(x) for x in subvalue)}</{subkey}>"
                   if type(subvalue) is dict:
                      #print(subkey,type(subvalue),'--------------->',subvalue)
                      buttons = subvalue.get('button', [])
                      if buttons:
                         print(buttons)
                         for button in buttons:
                             print(button['@string'])   
                             tag=button['@string']
                             fclass=button['@class']
                             html +=f'<button class="{fclass}">{tag}</button>'
                             print('000000000000000000')
                         #isinya = buttons.get('@string', None)
                         
                elif isinstance(subvalue, dict):
                    html += generate_html(subvalue)  # Recursion for nested dictionaries
                html += f"</{subkey}>"
        else:
            html += str(value)  # Handle non-dictionary values directly
        html += f"</{key}>"
    return html

html = generate_html(my_dict)
#print('generate------------------------------------')
print(html)

def generate_html2(my_dict):
    def process_value(key, value):
        if isinstance(value, dict):
            return generate_html(value)
        else:
            return f"{key}>{value}</{key}>"

    html = ""
    for key, value in my_dict.items():
        if key == 'group':
            html += f"<group>"
        else:
            html += f"<{key}>"
        
        if isinstance(value, dict):
            for subkey, subvalue in value.items():
                html += f"<{subkey}>"
                
                if isinstance(subvalue, list):
                    for item in subvalue:
                        html += process_value(subkey, item)
                else:
                    html += process_value(subkey, subvalue)
                
                html += f"</{subkey}>"
        else:
            html += process_value(key, value)

        if key == 'group':
            html += "</group>"
        else:
            html += f"</{key}>"
    
    return html

html = generate_html2(my_dict)
#print('generate------------------------------------')
#print(html)

# import odoorpc
import yaml
import logging
import pickle
from odoorpc import ODOO
import base64

from odooclient import OdooClient

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
# print(client)
myodo=OdooClient("localhost","8015",'felino','ninofelino12@gmail.com','felino')
print(myodo.company())    
# import odoorpc
import yaml
import logging
import pickle
from odoorpc import ODOO
import base64


class MyOdooClient(ODOO):
    '''
      
    '''  
    
    def __init__(self, server,port,dbname):
        super(MyOdooClient, self).__init__(server, port=port)
        self.login(dbname, user, password)
        

    def user(self):
        """
        This method is a custom method that is added to the class.
        """

        return self.odoo.env.user
    def f_execute(self,models,type):
        with open('model.yaml', "r") as f:
             data = yaml.load(f, Loader=yaml.FullLoader)
      
        
        # oo
        if type=="jpg":
            field="avatar_128"
            record = super().env[data[models]['model']].search([('id', '=', 15)])
            partner_data = record[0]
            #image_data = partner_data.get('avatar_128')
            result=self.execute(data[models]['model'], 'read',record,[field])  
            return base64.b64decode(result[0].get(field))
        else:
            field=data[models]['field'].split(',')
            record=super().env[data[models]['model']].search([])
            result=self.execute(data[models]['model'], 'read',record,field)    
            return result
    def image():
        return "image"  
    def save():
        serialized_object = pickle.dumps(MyOdooClient)
        with open('object.class', 'wb') as file:
            file.write(serialized_object)



# Prepare the connection to the server

server = 'localhost'
port = '8015'
dbname = 'felino'
user = 'ninofelino12@gmail.com'
password = 'felino'


serialized_object = pickle.dumps(MyOdooClient)
with open('felino.class', 'wb') as file:
    file.write(serialized_object)


with open('object.class', 'rb') as file:
    serialized_object = file.read()

loaded_obj = pickle.loads(serialized_object)
loaded_obj.save()   

hasil=loaded_obj("localhost","8015",'felino')

client=hasil.f_execute('product.product','json')
print(client)

image=hasil.f_execute('res.partner','jpg')
print(image)
with open('avatar_image.png', 'wb') as image_file:
    image_file.write(image)
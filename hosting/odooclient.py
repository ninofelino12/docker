# import odoorpc
import yaml
import logging
import pickle
from odoorpc import ODOO,report
from odoo_rpc_client import Client

import base64


class OdooClient(ODOO):
    '''
      
    '''  
    
    def __init__(self, server,port,dbname,user,password):
        super(OdooClient, self).__init__(server, port=port)
        self.login(dbname, user, password)
        

    def user(self):
        """
        This method is a custom method that is added to the class.
        """

        return self.odoo.env.user
    

    def nav(self):
        with open('model.yaml', "r") as f:
             data = yaml.load(f, Loader=yaml.FullLoader)
             links = [value['name'] for value in data.values()] 
             combined_list = [(data[key]['name'], data[key]['model']) for key in data]
             html_links = ['<a href="/model/{}">{}</a>'.format(model, name) for name, model in combined_list]
             html_string = ''.join([f'<a href="">{link}</a>' for link in links])

             html_links_string = ''.join(['<button onclick="getContent(\'{}\',\'html\')">{}</button>'.format(model,name) for name, model in combined_list])
             model_name =  data.get('name')
             model_model = data.get('model')
            #  print(f"Name: {model_name}")
            #  print(f"Model: {model_model}")
            # namesw = [data[key]['name'] for key in data]
            # models = [data[key]['model'] for key in data]
            
        return html_links_string 
    
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
        elif type=="xml":
            field="arch_base"
            record = super().env[data[models]['model']].search([('id', '=', 4)])
            partner_data = record[0]
            result=self.execute(data[models]['model'], 'read',record,[field])  
            return result[0].get(field)
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

    def has_key(item,key):
        return key in item

    def ubah_key(item,model):
        if self.has_key(item,'avatar_128'):
            item['avatar_128']=f'<img src="image?id={item["id"]}&model={model}"/>'
        if self.has_key(item,'image_128'):
            item['image_128']=f'<img src="image?id={item["id"]}&model={model}"/>'     
        return item

    def company(self):
        user = super().env.user
        # print(user.name)            # name of the user connected
        # print(user.company_id.name)
        # print(dir(user))
        
        # print(user.company_id.email)
        # print(user.company_id.website_url)
        # print(user.company_id.phone)
        # print(user.company_id.street)
        # print(dir(user.company_id.message_unread))
        reports = super().report.list()
        print(dir(report)) 
        #report_data = super().report('repor').get_pdf([212])
        client = Client("localhost:8015", 'felino','ninofelino@gmail.com','felino')
        print(dir(client))
        report_list = client.report.list()
        for report_info in report_list:
            print("Report ID:", report_info.get('id'))
            print("Report Name:", report_info.get('name'))
            print("Report Model:", report_info.get('model'))
            print("-------------")
        return "info"
# Prepare the connection to the server


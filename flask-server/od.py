import odoorpc
import json



class Odoofelino:
    server='203.194.112.105'
    userid=0
    db=[]
    myresponse=''
    model='res.users'
    odoo = odoorpc.ODOO(server, port=80)
    user=''
    field=fields='id,name'.split(',') 
    def login(self):
        server='203.194.112.105'
        odoo=self.odoo
        self.odoo.login('DEMO', 'admin', 'odooadmin')
        self.user = self.odoo.env.user
       

    def get(self):
        
        Order = self.odoo.env[self.model]
        order_ids = Order.search([])
        partner_data = []
        for order in Order.browse(order_ids):
            template={'name':order.name,'id':order.id}
            partner_data.append(template)
        self.myresponse=json.dumps(partner_data)    
        
        print(self.myresponse)
           
        
    def db(self):
        self.database=self.odoo.db.list()
    def info(self):
        print('------------------------------------') 
        print(self.odoo.db.list())   
        print(self.myresponse)    
        
odoo = Odoofelino()
odoo.model='res.partner'
odoo.login()
# print(odoo.db)
odoo.get()

#odoo.info()

import odoorpc
import json



class Odoofelino:
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
        self.odoo = odoorpc.ODOO(server, port=port)
        self.login()
        
    def login(self):
        # server='203.194.112.105'
        # odoo=self.odoo
        self.odoo.login('DEMO', 'admin', 'odooadmin')
        self.user = self.odoo.env.user
       

    def getold(self):
        
        Order = self.odoo.env[self.model]
        order_ids = Order.search([])
        partner_data = []
        for order in Order.browse(order_ids):
            template={'name':order.name,'id':order.id}
            partner_data.append(template)
        self.myresponse=json.dumps(partner_data)    
        records=Order.browse(order_ids)
        COBA = json.dumps([
        {'name': record.name, 'id': record.id}  # Buat dict langsung dalam list comprehension
        for record in records
        ])    
        print(self.myresponse)
    
    def get(self):
        model = self.odoo.env[self.model]
        Order = self.odoo.env[self.model]
        records = model.search([])
        order_ids = Order.search([])
        records=Order.browse(order_ids)
        record_data = []
        for record in records:
            record_dict = {'name': record.name, 'id': record.id}
            record_data.append(record_dict)
        self.myresponse = json.dumps(record_data)
    
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
    
    def getnew(self):
        
        Order = self.odoo.env[self.model]
        order_ids = Order.search([])
        partner_data = []
        records=Order.browse(order_ids)
        self.myresponse = json.dumps([
        {'name': record.name, 'id': record.id}  # Buat dict langsung dalam list comprehension
        for record in records
        ])    
        # print(self.myresponse)
    

    
        
    def db(self):
        #Caching
        if self._databases is None:
            self._databases = self.odoo.db.list()
        return self.odoo.db.list()
    def info(self):
        print('------------------------------------')
        print(self.odoo.db.list(), self.myresponse)
        
odoo = Odoofelino(model='res.partner')
odoo.login()
# print(odoo.db)
#odoo.get3()
print(odoo.getfel(['name']))
print(odoo.getfel())
print(odoo.myresponse)

#odoo.info()

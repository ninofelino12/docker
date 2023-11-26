import xmlrpc.client


class OdooClient:
    def __init__(self, url, db, username, password):
        self.url = url
        self.db = db
        self.username = username
        self.password = password
        self.common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(self.url))
        self.uid = self.common.authenticate(self.db, self.username, self.password, {})

        if self.uid:
            self.models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(self.url))

    def search_records(self, model, domain=None, offset=0, limit=None, order=None):
        if not self.uid:
            print("Authentication failed. Please check your credentials.")
            return []

        if not limit:
            limit = 0  # Unlimited records

        if not order:
            order = "id desc"  # Default order

        records = self.models.execute_kw(
            self.db, self.uid, self.password,
            model, 'search_read',
            [domain],
            {'fields': [], 'offset': offset, 'limit': limit, 'order': order}
        )
        return records
    def product(self):
        product_ids = self.models.execute_kw(self.db,self.uid,self.password,'product.product','search', [[]],    {'limit': 5})
        products = self.models.execute_kw(self.db,self.uid,self.password,'product.product','read',[product_ids],{'fields': ['name', 'list_price']})  
                                     

# Menampilkan hasil
        hasil=""
        for product in products:
        
            print(f"Nama Produk: {product['name']}, Harga: {product['list_price']}")
            hasil=hasil+"<tr><td>"+f"Nama Produk: {product['name']}, Harga: {product['list_price']}"+"</td></tr>"
        return hasil  


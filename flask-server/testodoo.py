from OdooClient import OdooClient

url = 'http://203.194.112.105:80'
db = 'demo-01'
username = 'admin'  
password = 'odooadmin'

odoo_client=OdooClient(url,db, username, password)

# Contoh penggunaan untuk mencari beberapa catatan dari model tertentu
records = odoo_client.search_records('res.partner',domain=[('is_company', '=', False)],limit=100)
tabel=[]
for record in records:
    print(record['id'],record['name'])
    tabel.append([record['id'],record['name']])
print(tabel)    

from flask import Flask
from flask import render_template
import odoo_connect
import xmlrpc.client

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html', title='Home Page')
@app.route('/odoo')
def odooc():
    url = 'http://203.194.112.105:8000'
    db = 'demo-01'
    username = 'admin'  
    password = 'odooadmin'

    common = xmlrpc.client.ServerProxy(f'{url}/xmlrpc/2/common')
    uid = common.authenticate(db, username, password, {})
    user_model = "res.users"
    models = xmlrpc.client.ServerProxy(f"{url}/xmlrpc/2/object")
    user_ids = models.execute_kw(db, uid, password, user_model, "search", [[]])
    users = models.execute_kw(db, uid, password, user_model, "search_read", [[]], {'fields': ['name', 'login', 'email']})

# Menampilkan data pengguna
    for user in users:
        print(f"User Name: {user['name']}, Login: {user['login']}, Email: {user['email']}")
        for key, value in user.items():
            print("------------------------")
            print(f"{key}: {value}")
    print(uid)
    #odoo = env = odoo_connect.connect(url=url, username=username, password='password')
    #so = env['sale.order']
    #so.search_read([('create_uid', '=', 1)], [])
    return render_template('index.html', title='Home Page',user="felino")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0',port=4000)

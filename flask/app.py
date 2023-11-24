from flask import Flask
from flask import render_template
#import odoo_connect
#import xmlrpc.client

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html', title='Home Page')
@app.route('/odoo')
def od():
    return render_template('index.html', title='Home Page',user="felino")
@app.route('/serial')
def serial():
    return render_template('serial.html', title='Home Page',user="felino")
@app.route('/docker')
def docker():
    return render_template('docker.html', title='Home Page',user="felino")
@app.route('/iot')
def iot():
    return render_template('iot.html', title='Home Page',user="felino")
@app.route('/hosting')
def hostinger():
    return render_template('hosting.html', title='Home Page',user="felino")


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0',port=4000)

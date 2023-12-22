import odoorpc
import pickle
import base64


# Koneksi ke server Odoo
odoo = odoorpc.ODOO('localhost', port=8015)

odoo.login('felinosample', 'ninofelino12@gmail.com', 'felino')
product_id = 1
product = odoo.env['product.template'].read(product_id, ['image_128'])
isi=product
print(isi)
# Menyimpan data gambar ke file
# with open('product_image.png', 'wb') as f:
#     f.write(base64.decodebytes(isi))
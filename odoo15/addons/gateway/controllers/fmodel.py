import odoorpc
def showmodel(model="product.product",id=0,result=['name','id'],jenis="data"):
    odoo = odoorpc.ODOO('localhost', port=8015)
    odoo.login('felino', 'ninofelino12@gmail.com', 'felino')
    hasil=""
    Order=odoo.env[model]
    hasil_data = []
    order_ids = Order.search([]) if id == 0 else id

    for order in Order.browse(order_ids):
        if jenis=="png":
           hasil_data.append({order.image_1920}) 
        else:    
           hasil_data.extend([order[item] for item in result])
     
    return hasil_data


result_data = showmodel(model="res.partner", id=1, result=['name', 'id','comment','display_name'], jenis="data")
print(result_data)
hasil=showmodel(jenis="png")
hasil=showmodel(result=['name','code'])
print(hasil)
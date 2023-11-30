
menu_items = [
    {"name": "Home", "url": '//iot/home'},
    {"name": "Left", "url": '//iot/left'},
    {"name": "Right", "url": '//iot/right'}
]

# To access the values, you can iterate through the list
hasil=""
for item in menu_items:
    hasil=hasil+f"<a href=\"{item['url']}\" /> {item['name']}</a>"
print(hasil)    
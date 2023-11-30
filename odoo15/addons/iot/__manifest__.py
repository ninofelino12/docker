# -*- coding: utf-8 -*-
{
    'name': "Iot",

    'summary': """
            Internet of Things, 
            """,

    'description': """
        
        Internet of Things, merujuk pada jaringan perangkat 
        fisik yang saling terhubung dan bertukar data melalui internet. Perangkat 
        IoT, atau sering disebut sebagai "things," dilengkapi dengan sensor, 
        perangkat lunak, dan teknologi lainnya untuk mengumpulkan dan bertukar data. 
        Contoh aplikasi IoT melibatkan penggunaan sensor dalam berbagai bidang seperti rumah pintar, 
        kesehatan, pertanian, dan industri untuk menghasilkan informasi yang berharga dan 
        mendukung pengambilan keputusan berbasis data. 
    """,

    'author': "NinoFelino",
    'website': "https://ninofelino12.github.io/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Services',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','web'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
         'security/ir.model.access.csv',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'auto_install': False,
    'assets': {
        'web.assets_frontend': [
            'iot/static/src/iot.css',
        ],
    },
}

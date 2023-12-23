# -*- coding: utf-8 -*-
{
    'name': "felcore",

    'summary': """
        core system untuk pengembangan Odoo meliputi static file
        template html 
        """,    
    'description': """
        Long description of module's purpose
    """,

    'author': "ninofelino12@github.io",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        # 'views/login.xml',
       
    
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    #'qweb': ['static/src/xml/my_module_template.xml'],
    'auto_install': False,
    'installable': True,
    
},
}

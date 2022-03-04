# -*- coding: utf-8 -*-
{
    'name': "moduloArtistasObrasEtc",

    'summary': """
        el tonto del hugo""",

    'description': """
        my module is expiration management
    """,

    'author': "El rc y el vecino",
    'website': "http://www.expirationManagement.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Modulo basic',
    'version': '0.0.0.0.0.0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        # 'views/views.xml',
        # 'views/templates.xml',
        'views/painting.xml',
        'views/artistas.xml',
        'reports/artistas_report.xml',
        'reports/obras_report.xml',
    ],
    # only loaded in demonstration mode
    # 'demo': [
    #   'demo/demo.xml',
    # ],
}

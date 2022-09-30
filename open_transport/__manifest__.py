# -*- coding: utf-8 -*-
{
    'name': "OpenTransport",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Human Resources',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','fleet','product', 'account'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/trajets_views.xml',
        'views/trajets_list_custom_views.xml',
        'views/villes_views.xml',
        'views/assurance_view.xml',
        'views/dossier_views.xml',
        'views/facturation_elem_views.xml',
        'views/res_partner_views.xml',
        'sequence/trajet_sequence.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
        'installable': True,
    'application': True,
    'assets': {
        'web.assets_backend': [
            'open_transport/static/src/**/*',
        ],
    },
    'license': 'LGPL-3',

}

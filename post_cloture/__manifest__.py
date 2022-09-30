# -*- coding: utf-8 -*-
{
    'name': "Post Cloture",

    'summary': """
        """,

    'description': """
        
    """,

    'author': "Montaigne",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'sale',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','point_of_sale'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/post_cloture_sexion_line_views.xml',
        'views/post_cloture_sexion_views.xml',
        'views/post_cloture_sexion_synthese_view.xml',
        'report/pos_cloture_template.xml',
        'report/report_pos_cloture.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

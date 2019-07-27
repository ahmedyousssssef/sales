# -*- coding: utf-8 -*-
{
    'name': "sales_customiz",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base' , 'sky_height' , 'isky_access_rights' , 'sale',
                'crm',
                'sale_crm',],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'security/sales_groups.xml',
        'views/skay_heights_menus.xml',
        'views/welcome_card_view.xml',
        'views/reservation_view.xml',
        'views/customer_view.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
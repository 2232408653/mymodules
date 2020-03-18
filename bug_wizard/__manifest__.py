# -*- coding: utf-8 -*-
{
    'name': "bug_wizard",

    'summary': """
        bug管理辅助使用模块
    """,

    'description': """
        bug管理辅助使用模块
    """,

    'author': "DS",
    'website': "http://odoo12.xyz",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['ds_bug'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/bug_wizard.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

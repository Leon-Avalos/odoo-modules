# -*- coding: utf-8 -*-
{
    'name': "Open Academy",

    'summary': """Manage trainings""",

    'description': """
        Module for managing trainings:
            -training coures
            -training sessions
            -attendees registration 
    """,

    'author': "Leon Avalos",
    'website': "http://www.leonavalos.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Test',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/openacademy.xml'
        #'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
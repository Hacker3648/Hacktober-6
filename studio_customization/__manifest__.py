# -*- coding: utf-8 -*-

{
    'name': 'Custom Studio',
    'version': '17.0',
    'summary': '',
    'author': 'Sunil Prajapati',
    'sequence': 2,
    'description': """ """,
    'category': '',
    'images': ['static/description/icon.png'],
    'depends': ['website','web','crm'],
    'data': [
        'security/ir.model.access.csv',
        'views/crm_lead.xml',
        'views/diabetes_registration.xml',
        'views/thank_you.xml',
    ],
    'assets':{
        'web.assets_frontend': [
            'studio_customization/static/src/js/globle.js',
            'studio_customization/static/src/scss/select2.scss',
        ],
    },
    'license': 'LGPL-3',
    'installable': True,
    'application': True,
    'auto_install': False,
}

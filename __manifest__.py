# -*- coding: utf-8 -*-
{
    'name': 'Accounting Edit Sequence Number',
    
    'author' : 'Softhealer Technologies',
    
    'website': 'https://www.softhealer.com',    
    
    "support": "info@softhealer.com",   
        
    'version': '10.0.2',
    
    'category': 'Extra Tools',

    'summary': 'Edit sequence number of sales purchase accounting',

    'description': """Currently in odoo you can not edit sequence number of accounting stuff. This module help user to edit sequence number in accounting (invoice bills credit debit notes.).""",
    
    'depends': ['account'],
    
    'data': [
            'data/edit_sequence.xml',
            'views/account_invoice.xml',
            'views/report_invoice.xml',
            ],
    
    'images': ['static/description/background.png',],              
    
    'auto_install': False,
    'installable' : True,
    'application': True,    
    
    "price": 20,
    "currency": "EUR"        
}

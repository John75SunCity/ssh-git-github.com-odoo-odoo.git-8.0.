# -*- coding: utf-8 -*-
{
    'name': 'Records Management',
    'version': '18.0.1',
    'license': 'OPL-1',
    'depends': [
        'base',
        'stock',
        'web',
        'mail',
        'portal',
        'board',
        'product',
        'contacts'
    ],
    'summary': 'Centralized records storage, search, permissions, and audit trails.',
    'description': '''
Records Management
==================
A comprehensive module for managing records in Odoo.

Features:
- Centralized record storage
- Easy search and retrieval
- Access control and permissions
- Audit trails and history tracking
- Integration with stock and web modules
- Demo data and scheduled actions for testing

**Note:** This app does not collect or transmit user data outside Odoo.
''',
    'website': 'https://suncityshred.com',
    'category': 'Tools',
    'icon': 'records_management/static/description/icon.png',
    'data': [
        'views/inventory_template.xml',
        'views/pickup_request.xml',
        'views/my_portal_inventory.xml',
        'views/shredding_views.xml',
        'security/groups.xml',
        'security/ir.model.access.csv',
        'data/products.xml',
        'data/scheduled_actions.xml',
        'data/scrm_records_management_data.xml'
    ],
    'installable': True,
    'application': True
}
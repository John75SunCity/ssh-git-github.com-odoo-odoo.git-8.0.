{
    'name' : 'Odoo Live Support',
    'author': 'OpenERP SA',
    'version': '8.0.1',
    'summary': 'Chat with the Odoo collaborators',
    'category': 'Tools',
    'complexity': 'medium',
    'website': 'https://www.odoo.com/',
    'description':
        """
Odoo Live Support
=================

Ask your functionnal question directly to the Odoo Operators with the livechat support.

        """,
    'data': [
        "views/im_odoo_support.xml"
    ],
    'depends' : ["web", "im_chat"],
    'qweb': [
        'static/src/xml/im_odoo_support.xml'
    ],
    'installable': True,
    'auto_install': True,
    'application': True,
    'license': 'LGPL-3',
}

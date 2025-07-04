# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################


{
    'name': 'Point of Sale Discounts',
    'version': '1.0',
    'category': 'Point of Sale',
    'sequence': 6,
    'summary': 'Simple Discounts in the Point of Sale ',
    'description': """

=======================

This module allows the cashier to quickly give a percentage
sale discount to a customer.

""",
    'author': 'OpenERP SA',
    'depends': ['point_of_sale'],
    'data': [
        'views/views.xml',
        'views/templates.xml'
    ],
    'installable': True,
    'website': 'https://www.odoo.com/page/point-of-sale',
    'auto_install': False,
    'license': 'LGPL-3',
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:

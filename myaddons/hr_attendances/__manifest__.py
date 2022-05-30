# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.


{
    'name': 'Attendances Extended',
    'version': '2.0',
    'category': 'Human Resources/Attendances',
    'sequence': 81,
    'summary': 'Track employee attendance',
    'description': """
This module aims to manage employee's attendances.
==================================================

Keeps account of the attendances of the employees on the basis of the
actions(Check in/Check out) performed by them.
       """,
    'website': 'https://www.odoo.com/page/employees',
    'depends': ['hr_attendance', 'base', 'hr'],
    'data': [
        'views/admin_attendances.xml',
        'views/manager_employees_attendance.xml',
        'views/reporting.xml'
    ],
    'demo': [
    
    ],
    'installable': True,
    'auto_install': False,
    'qweb': [
        "static/src/xml/attendance.xml",
    ],
    'application': True,
    'license': 'LGPL-3',
}

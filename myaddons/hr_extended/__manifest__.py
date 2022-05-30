# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Employees extended',
    'version': '1.1',
    'category': 'Human Resources/Employees',
    'sequence': 75,
    'summary': 'Centralize employee information',
    'description': "",
    'website': 'https://www.odoo.com/page/employees',
    'images': [
        'images/hr_department.jpeg',
        'images/hr_employee.jpeg',
        'images/hr_job_position.jpeg',
        'static/src/img/default_image.png',
    ],
    'depends': [
        'hr',
        'base'
    ],
    'data': [
        'views/hr_employee_views.xml',
        'views/hr_employees_directory.xml'
    ],
    'demo': [
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'qweb': ['static/src/xml/hr_templates.xml'],
    'license': 'LGPL-3',
}

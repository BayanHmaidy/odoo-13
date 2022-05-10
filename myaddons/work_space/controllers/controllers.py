# -*- coding: utf-8 -*-
from re import U
from odoo import http
from odoo.http import request
import json
class User(http.Controller):
    @http.route('/user/create/', type='json', auth='public', methods=['POST', 'OPTIONS'],  csrf=False, cors='*')
    def create_user(self, **user):
        body= json.loads(request.httprequest.data)
        user = body.get('user')
        
        existed_user = http.request.env['res.users'].sudo().search([('login', '=', user['email'])])
        if(existed_user): 
            return {
                "status_code": 409,
                "details": "Bad request email already exists"
            }
        
        # create partner
        partner = request.env['res.partner'].sudo().create({
            'name': f"{user['first_name']} {user['last_name']}"
        })

        # create new user
        created_user = request.env['res.users'].sudo().create({
            'name': f"{user['first_name']} {user['last_name']}",
            'login': user['email'],
            'mobile': user['mobile'],
            'password': user['password'],
            'company_id': user['company_id'],
            'partner_id': partner.id,
            'active': True,
            'email': user['email'],
            'sel_groups_17_18_19': 17,
            'sel_groups_15_13_14': 15,
            'tz': 'Asia/Amman'
            })

        # create employee
        employee = http.request.env['hr.employee'].sudo().create({
            'name': f"{user['first_name']} {user['last_name']}",
            "company_id": user['company_id'],
            'user_id': created_user.id,
            'starting_date': user['starting_date']
            })

        paid_allocation = http.request.env['hr.leave.allocation'].sudo().create({
            'name': 'paid time off',
            'holiday_status_id': 1,
            'allocation_type': 'accrual',
            'number_per_interval': 9.20547936,
            'unit_per_interval': 'hours',
            'interval_number': 1,
            'interval_unit': 'months',
            'number_of_days': 0.00,
            'holiday_type': 'employee',
            'employee_id': employee.id
        })

        paid_allocation.action_approve()
        paid_allocation.action_validate()

        unpaid_allocation = http.request.env['hr.leave.allocation'].sudo().create({
            'name': 'unpaid time off',
            'holiday_status_id': 4 ,
            'allocation_type': 'accrual',
            'number_per_interval': 9.20547936,
            'unit_per_interval': 'hours',
            'interval_number': 1,
            'interval_unit': 'months',
            'number_of_days': 0.00,
            'holiday_type': 'employee',
            'employee_id': employee.id
        })

        unpaid_allocation.action_approve()
        unpaid_allocation.action_validate()
    

        # for allocation in range(14):
        sick_allocation = http.request.env['hr.leave.allocation'].sudo().create({
            'name': 'sick time off',
            'holiday_status_id': 2,
            'allocation_type': 'regular',
            'number_of_days': 14,
            'holiday_type': 'employee',
            'employee_id': employee.id,
        })

        sick_allocation.action_approve()
            # sick_allocation.action_validate()

        return {
            'status_code': 200,
            'user_id': created_user.id,
            'name': f"{user['first_name']} {user['last_name']}",
            'login': user['email'],
            'mobile': user['mobile'],
            'company_id': user['company_id'],
            'active': True
            }
       

    @http.route('/user/<int:user_id>', type="json", auth='public', methods=['GET', 'OPTIONS'],  csrf=False, cors='*')
    def get_user(self, user_id):
        # get user info
        user = http.request.env['res.users'].sudo().browse(user_id)
        if user.exists():
            employee = http.request.env['hr.employee'].sudo().browse(int(user.employee_id))
            first_name, last_name = user.name.split(" ")
            # get compnay info
            company = http.request.env['res.company'].sudo().browse(int(user.company_id))
            return {
                "status_code": 200,
                "user_id": user.id, 
                "first_name": first_name,
                "last_name": last_name,
                "email": user.login,
                "mobile": user.mobile,
                "company_name": company.name,
                "active": user.active,
            }
        return {
            "status_code": 404,
            "details": "User not found"
        }

    @http.route('/user/update/<int:user_id>', type="json", auth='public', methods=['PUT', 'OPTIONS'], csrf=False, cors='*')
    def update_user(self, user_id):

        body= json.loads(request.httprequest.data)
        parameters = body.get('user')
        
        user = http.request.env['res.users'].sudo().browse(user_id)
        if user.exists():
            if parameters.get('first_name') or parameters.get('last_name'):
                current_first_name, current_last_name = user.name.split(" ")
                first_name = parameters.get('first_name') or current_first_name
                last_name = parameters.get('last_name') or current_last_name
                parameters['name'] = f"{first_name} {last_name}"

                if parameters.get('first_name'):
                    del parameters['first_name']
                if parameters.get('last_name'):
                    del parameters['last_name']
            user.write(parameters)
            parameters['status_code'] = "201"
            return parameters

        return {
            "status_code": 404,
            "details": "User not found"
        }


    @http.route('/user/deactivate/<int:user_id>', type="json", auth='public', methods=['PUT', 'OPTIONS'], csrf=False, cors='*')
    def deactivate_user(self, user_id):
        user = http.request.env['res.users'].sudo().browse(user_id)
        employee = http.request.env['hr.employee'].sudo().browse(int(user.employee_id))
        if user.exists():
            user.write({"active": False})
            employee.write({"active": False})
            return (user.active, employee.active)
        return {
            "status_code": 404,
            "details": "User not found"
        }
        
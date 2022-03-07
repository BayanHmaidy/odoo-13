# -*- coding: utf-8 -*-
from re import U
from odoo import http
from odoo.http import request, Response
import json
class User(http.Controller):
    @http.route('/user/create/', type='json', auth='public', methods=['POST', 'OPTIONS'],  csrf=False, cors='*')
    def create_user(self, **user):
        body= json.loads(request.httprequest.data)
        user = body.get('user')
        
        existed_user = http.request.env['res.users'].sudo().search([('login', '=', user['email'])])
        if(existed_user): 
            Response.status = "409" 
            return ("Bad request, email already exists")

        # create new user
        created_user = http.request.env['res.users'].sudo().create({
            'name': f"{user['first_name']} {user['last_name']}",
            'login': user['email'],
            'mobile_phone': user['mobile_phone'],
            'password': user['password'],
            'company_id': user['company_id'],
            'active': True
            })

        # create employee
        http.request.env['hr.employee'].sudo().create({
            'name': f"{user['first_name']} {user['last_name']}",
            "company_id": user['company_id'],
            'user_id': created_user.id,
            'active': True
            })

        return {
            'user_id': created_user.id,
            'name': f"{user['first_name']} {user['last_name']}",
            'login': user['email'],
            'mobile_phone': user['mobile_phone'],
            'password': user['password'],
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
                "user_id": user.id, 
                "first_name": first_name,
                "last_name": last_name,
                "email": user.login,
                "mobile_phone": user.mobile_phone,
                "company_name": company.name,
                "active": user.active,
            }
        Response.status = "404" 
        return ("User not found")    

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
            return parameters

        Response.status = "404" 
        return ("User not found")


    @http.route('/user/deactivate/<int:user_id>', type="json", auth='public', methods=['PUT', 'OPTIONS'], csrf=False, cors='*')
    def deactivate_user(self, user_id):
        user = http.request.env['res.users'].sudo().browse(user_id)
        employee = http.request.env['hr.employee'].sudo().browse(int(user.employee_id))
        if user.exists():
            user.write({"active": False})
            employee.write({"active": False})
            return (user.active, employee.active)
        return {"messsage": "Not found"}
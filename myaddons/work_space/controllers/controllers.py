# -*- coding: utf-8 -*-
from crypt import methods
from odoo import http
from odoo.http import request
import json


class UserCreation(http.Controller):
    @http.route('/user/create/', type='json', auth='public', methods=['POST', 'OPTIONS'],  csrf=False, cors='*')
    def create_user(self, **params):
        body= json.loads(request.httprequest.data)
        params = body.get('parms')
        res = http.request.env['res.users'].sudo().create({
            'name': params['name'],
            'login': params['email'],
            'password': params['password'],
            'company_id': 1
            })
        http.request.env['hr.employee'].sudo().create({
            'name': params['name'],
            "company_id": 1,
            'user_id': res.id
            })
        return body
        
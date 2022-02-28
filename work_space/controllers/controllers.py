# -*- coding: utf-8 -*-
from crypt import methods
from odoo import http
from odoo.http import request
import json


class Test(http.Controller):
    # @http.route('/test/test/', auth='public')
    # def index(self, **params):
    #     return "Hello, world"

    @http.route('/test/test/', website=True, auth='public')
    def index(self, **kw):
        return request.render("test.test", {
            'tests': ['test1', 'test2', 'test3']
        })
    
    @http.route('/create/', type='json', auth='public', methods=['POST', 'OPTIONS'],  csrf=False, cors='*')
    # @cross_origin()
    def create(self, **params):
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
        
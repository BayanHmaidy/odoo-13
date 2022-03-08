from odoo import http

def create_user(user):
    # create new user
    existed_user = http.request.env['res.users'].sudo().search([('login', '=', '446ff6')])
    if(existed_user): 
        return '400 Bad Request'
    created_user = http.request.env['res.users'].sudo().create({
        'name': f"{user['first_name']} {user['last_name']}",
        'login': user['email'],
        'mobile_phone': user['mobile_phone'],
        'password': user['password'],
        'company_id': user['company_id'],
        'active': True
        })
    return created_user

# def create_employee(user):
#     created_user = create_user(user)
#     # create employee
#     http.request.env['hr.employee'].sudo().create({
#         'name': f"{user['first_name']} {user['last_name']}",
#         "company_id": user['company_id'],
#         'user_id': created_user.id,
#         'active': True
#         })



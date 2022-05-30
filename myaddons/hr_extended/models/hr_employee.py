from odoo import fields, models

class HrEmployee(models.Model):
    _inherit = 'hr.employee'

    address_home_id = fields.Many2one(string="Employee Address", groups="work_space.group_admin_access,work_space.group_manager_access")
    private_email = fields.Char(groups="work_space.group_admin_access,work_space.group_manager_access")
    bank_account_id = fields.Many2one(groups="work_space.group_admin_access,work_space.group_manager_access")
    phone = fields.Char(groups="work_space.group_admin_access,work_space.group_manager_access")
    km_home_work = fields.Integer(groups="work_space.group_admin_access,work_space.group_manager_access")
    country_id = fields.Many2one(groups="work_space.group_admin_access,work_space.group_manager_access")
    identification_id = fields.Char(groups="work_space.group_admin_access,work_space.group_manager_access")
    passport_id = fields.Char(groups="work_space.group_admin_access,work_space.group_manager_access")
    gender = fields.Selection(groups="work_space.group_admin_access,work_space.group_manager_access")
    birthday = fields.Date(groups="work_space.group_admin_access,work_space.group_manager_access")
    place_of_birth = fields.Char(groups="work_space.group_admin_access,work_space.group_manager_access")
    country_of_birth = fields.Many2one(groups="work_space.group_admin_access,work_space.group_manager_access")
    marital = fields.Selection(groups="work_space.group_admin_access,work_space.group_manager_access")
    study_school = fields.Char(groups="work_space.group_admin_access,work_space.group_manager_access")
    emergency_contact = fields.Char(groups="work_space.group_admin_access,work_space.group_manager_access")
    emergency_phone = fields.Char(groups="work_space.group_admin_access,work_space.group_manager_access")
    certificate = fields.Selection(groups="work_space.group_admin_access,work_space.group_manager_access")
    study_field = fields.Char(groups="work_space.group_admin_access,work_space.group_manager_access")
    study_school = fields.Char(groups="work_space.group_admin_access,work_space.group_manager_access")
    visa_no = fields.Char(groups="work_space.group_admin_access,work_space.group_manager_access")
    permit_no = fields.Char(groups="work_space.group_admin_access,work_space.group_manager_access")
    visa_expire = fields.Date(groups="work_space.group_admin_access,work_space.group_manager_access")
    pin = fields.Char(groups="work_space.group_admin_access,work_space.group_manager_access")
    barcode = fields.Char(groups="work_space.group_admin_access,work_space.group_manager_access")
    children = fields.Integer(groups="work_space.group_admin_access,work_space.group_manager_access")
    
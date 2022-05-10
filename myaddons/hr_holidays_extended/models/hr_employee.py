from odoo import fields, models
from datetime import datetime


class HrEmployeeBase(models.AbstractModel):
    _inherit = "hr.employee.base"

    starting_date = fields.Datetime('Starting Date', readonly=False)

    def _get_date_start_work(self):
        return self.starting_date
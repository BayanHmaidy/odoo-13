from odoo import fields, models
from datetime import datetime
import time

class hr_leave(models.Model):
    _inherit = "hr.leave.type"

    def _today_date(self):
        for record in self:
            record ['validity_start'] = datetime.now()

    validity_start = fields.Date("From",
                                 help='Adding validity to types of time off so that it cannot be selected outside this time period',
                                 readonly=False,
                                 stored=True,
                                 compute='_today_date')
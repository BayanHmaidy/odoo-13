from odoo import fields, models

class hr_leave_report_calendar_extended(models.Model):
    _inherit = "hr.leave.report.calendar"

    def _prepare_holidays_meeting_values(self):
        result = []
        company_calendar = self.env.company.resource_calendar_id
        for holiday in self:
            calendar = holiday.employee_id.resource_calendar_id or company_calendar
            if holiday.leave_type_request_unit == 'hour':
                meeting_name = _("%s on time off : %.2f hour(s)") % (holiday.employee_id.employee_id or holiday.category_id, holiday.number_of_hours_display)
            else:
                meeting_name = _("%s on Time Off : %.2f day(s)") % (holiday.employee_id.employee_id or holiday.category_id, holiday.number_of_days)
            meeting_values = {
                'name': meeting_name,
                'duration': holiday.number_of_days * (calendar.hours_per_day or HOURS_PER_DAY),
                'description': holiday.notes,
                'user_id': holiday.user_id.id,
                'start': holiday.date_from,
                'stop': holiday.date_to,
                'allday': False,
                'state': 'open',  # to block that meeting date in the calendar
                'privacy': 'confidential',
                'event_tz': holiday.user_id.tz,
                'activity_ids': [(5, 0, 0)],
            }
            # Add the partner_id (if exist) as an attendee
            if holiday.user_id and holiday.user_id.partner_id:
                meeting_values['partner_ids'] = [
                    (4, holiday.user_id.partner_id.id)]
            result.append(meeting_values)
        return result
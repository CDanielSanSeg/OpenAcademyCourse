from odoo import models, fields, api
from odoo.exceptions import ValidationError
from dateutil.relativedelta import relativedelta


class Session(models.Model):
    _name = 'openacademy.session'
    _description = 'This is the Session model'

    active = fields.Boolean(default=True)
    attendees_ids = fields.Many2many("res.partner")
    attendees_number = fields.Integer(compute='_compute_attendees_number',  store=True)
    course_id = fields.Many2one("openacademy.course", required=True)
    description = fields.Text()
    duration = fields.Integer()
    end_date = fields.Datetime(compute='_compute_end_date')
    instructor_id = fields.Many2one(
        'res.partner',
        domain=[
            '|',
            ('instructor', '=', True),
            '&',
            ('category_id.name', 'ilike', 'level%'),
            ('category_id.parent_id.name', 'ilike', 'teacher')
        ]
    )
    name = fields.Char(required=True)
    number_of_seats = fields.Integer(default=1)
    percentage_of_seats_taken = fields.Float(compute='_compute_percentage_of_taken_seats', string="Seats %")
    start_date = fields.Datetime(default=fields.Date.context_today)

    @api.depends('attendees_ids')
    def _compute_attendees_number(self):
        for record in self:
            record.attendees_number = len(record.attendees_ids)

    @api.depends('start_date', 'duration')
    def _compute_end_date(self):
        for record in self:
            record.end_date = False
            if record.start_date and record.duration:
                record.end_date = record.start_date + relativedelta(days=record.duration)

    @api.depends('number_of_seats', 'attendees_ids')
    def _compute_percentage_of_taken_seats(self):
        for record in self:
            record.percentage_of_seats_taken = 0
            if record.number_of_seats > 0:
                record.percentage_of_seats_taken = (len(record.attendees_ids)/record.number_of_seats)*100

    @api.constrains('instructor_id', 'attendees_ids')
    def _check_instructor_not_in_attendees(self):
        for record in self.filtered('instructor_id'):
            if record.instructor_id in self.attendees_ids:
                raise ValidationError(f'The instructor "{record.instructor_id.name}" may not be an attendee')

    @api.onchange("number_of_seats", "attendees_ids")
    def _onchange_number_seats(self):
        if self.number_of_seats <= 0:
            return {
                'warning': {
                    'title': ('Incorrect seats value.'),
                    'message': ('The number of available seats must be greater than 0.'),
                }
            }
        if len(self.attendees_ids) > self.number_of_seats:
            return {
                'warning': {
                    'title': ('Attendees exceed the number of seats.'),
                    'message': ('There are not enough seats for all attendees.'),
                }
            }

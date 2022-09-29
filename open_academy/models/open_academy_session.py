from odoo import models, fields


class Session(models.Model):
    _name = 'openacademy.session'
    _description = 'This is the Session model'

    name = fields.Char(required=True)
    description = fields.Text()
    start_date = fields.Datetime(default=fields.Date.context_today)
    duration = fields.Integer()
    number_of_seats = fields.Integer()

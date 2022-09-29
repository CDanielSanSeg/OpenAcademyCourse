from odoo import models, fields


class Course(models.Model):
    _name = 'openacademy.course'
    _description = 'This is the Course model'

    title = fields.Char(required=True)
    description = fields.Text()

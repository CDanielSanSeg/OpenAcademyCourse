from odoo import models, fields


class ResPartner(models.Model):
    _inherit = "res.partner"

    instructor = fields.Boolean()
    sessions_ids = fields.Many2many("openacademy.session", string="Sessions")

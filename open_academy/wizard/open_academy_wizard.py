from odoo import models, fields


class OpenAcademyWizard(models.TransientModel):
    _name = 'openacademy.wizard'
    _description = 'Wizard model'

    session_id = fields.Many2one('openacademy.session', default=lambda self: self._default_session_id())
    attendees_ids = fields.Many2many('res.partner')

    def _default_session_id(self):
        return self.env['openacademy.session'].browse(self.env.context.get('active_ids'))

    def add_attendees(self):
        for record in self.session_id:
            record.attendees_ids |= self.attendees_ids

from odoo import _, models, fields


class Course(models.Model):
    _name = 'openacademy.course'
    _description = 'This is the Course model'
    _rec_name = "title"

    title = fields.Char(required=True)
    description = fields.Text()
    responsible_id = fields.Many2one('res.users')
    sessions_ids = fields.One2many("openacademy.session", "course_id")

    _sql_constraints = [
        (
            'check_course_diferente_to_description',
            'CHECK(title != description)',
            _('The course description cannot be the same as the course name.')
        ),
        (
            'check_course_unique',
            'UNIQUE(title)',
            _('This title already exist.')
        ),
    ]

    ''' This function copy a course '''
    def copy(self, default=None):
        default = dict(default or {})
        default.update({'title': f'Copy of {self.title}'})
        return super().copy(default=default)

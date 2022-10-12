from odoo.exceptions import ValidationError
from odoo.tests.common import TransactionCase


class GlobalTestOpenAcademySession(TransactionCase):
    """ This create global test to sessions """
    # Pseudo contructor method
    def setUp(self):
        super().setUp()
        self.session = self.env['openacademy.session']
        self.user_partner_demo = self.env.ref('base.res_partner_address_32')  # metadata of a user demo
        self.user_partner_atendee_demo = self.env.ref('base.res_partner_address_30')

    # Generic methods

    # Test methods
    def test_10_intructor_is_attendee(self):
        """ Check that raise of 'A sesion's instructor
        can't be an attendee'"""
        with self.assertRaisesRegex(
            ValidationError,
            f'The instructor "{self.user_partner_demo.name}" may not be an attendee'
        ):
            self.session.create(
                {
                    'name': 'Session test 1',
                    'number_of_seats': '1',
                    'instructor_id': self.user_partner_demo.id,
                    'attendees_ids': [(6, 0, [self.user_partner_demo.id])],  # for many2many
                    'course_id': self.env.ref('open_academy.course_f2').id,
                }
            )

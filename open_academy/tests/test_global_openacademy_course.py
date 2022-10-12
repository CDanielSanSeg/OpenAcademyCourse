from psycopg2 import IntegrityError
from psycopg2.errors import UniqueViolation

from odoo.tests.common import TransactionCase
from odoo.tools import mute_logger


class GlobalTestOpenAcademyCourse(TransactionCase):
    """ Global test for openacademy cours model.
    Test create course and trigger constraints. """
    # Method setup consturctor of test setUp
    def setUp(self):
        # Define global variables para test metods, it is like an __init__
        super().setUp()
        self.course = self.env['openacademy.course']

    # Method of class that is not test
    def create_course(self, course_name, course_description, course_responsible_id):
        # Create a course using parameter recived
        self.course.create(
            {
                'title': course_name,
                'description': course_description,
                'responsible_id': course_responsible_id,
            }
        )

    # Method of test startwith ' def test * self'
    # Mute the error openerp.sql_db to avoid it in log
    @mute_logger('odoo.sql_db')  # It is for mute the Error for bad query launched by odoo.sql_db
    def test_10_same_name_description(self):
        """ Test create a course with same name and description
        to raise constraint of name different to description. """

        # Error raised expected with message expected
        with self.assertRaisesRegex(
            IntegrityError,
            'new row for relation "openacademy_course" violates'
            ' check constraint "openacademy_course_check_course_diferente_to_description"'
        ):
            # Create a curse with the same name and description
            self.create_course('test', 'test', None)

    @mute_logger('odoo.sql_db')  # mute the error launched by a bad query
    def test_20_two_courses_same_name(self):
        """ Test to create two courses with same name
        to raise constraint of unique name. """

        self.create_course('test1', 'test_desciption', None)
        with self.assertRaisesRegex(
            UniqueViolation,
            'duplicate key value violates unique constraint'
            ' "openacademy_course_check_course_unique"'
        ):
            self.create_course('test1', 'test_desciption', None)

    def test_30_duplicate_course(self):
        """ Test to duplicate a course a and check that work fine! """
        course = self.env.ref('open_academy.course_f2')
        course.copy()

import unittest

from class_definitions import student_class as _student

"""" test.py for student_class.py"""


def test_inital_all_attributes():
    student1 = _student.Student('Anwary', 'Ihsan', 'BIS', 60.0)
    assert student1.last_name == 'Anwary'
    assert student1.first_name == 'Ihsan'
    assert student1.major == 'BIS'
    assert student1.gpa == 60.0


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.studen = _student.Student('Anwary', 'Ihsan', 'BIS', 60.0)

    def tearDown(self):
        del self.studen

    def test_initial_value_required_attributes(self):
        self.assertEqual(self.studen.last_name, 'Anwary')
        self.assertEqual(self.studen.first_name, 'Ihsan')

    def test_not_created_error_last_name(self):
        with self.assertRaises(ValueError):
            name = _student.Student('555', 'Ihsan', "BIS", 55.0)

    def test_created_error_fist_name(self):
        with self.assertRaises(ValueError):
            name = _student.Student('Anwary', '333', "BIS", 65.0)

    def test_created_error_major(self):
        with self.assertRaises(ValueError):
            name = _student.Student('Anwary', 'Ihsan', '55', 66.5)


if __name__ == '__main__':
    unittest.main()

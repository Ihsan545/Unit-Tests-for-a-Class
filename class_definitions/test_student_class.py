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




if __name__ == '__main__':
    unittest.main()

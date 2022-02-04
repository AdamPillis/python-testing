import unittest
from student import Student


class TestStudent(unittest.TestCase):
    """Test student methods"""

    @classmethod
    def setUpClass(cls):
        print('setUpClass')

    @classmethod
    def tearDownClass(cls):
        print('tearDownClass')

    def setUp(self):
        print('setUp')
        self.student = Student('John', 'Doe')

    def tearDown(self):
        print('tearDown')

    def test_full_name(self):
        """test for full name"""

        print('test_full_name')
        self.assertEqual(self.student.full_name, 'John Doe')

    def test_alert_santa(self):
        """test for santa list"""

        print('test_alert_santa')
        self.student.alert_santa()

        self.assertTrue(self.student.naughty_list)

    def test_email(self):
        """test for student email format"""

        self.assertEqual(self.student.email, 'john.doe@email.com')


if __name__ == '__main__':
    unittest.main()
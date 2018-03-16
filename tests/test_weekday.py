import unittest
from weekday import Weekday


class TestWeekDayMethods(unittest.TestCase):

    def test_square_days_attr(self):
        self.assertTrue(hasattr(Weekday('mon', '', 1), 'square'))
        self.assertTrue(hasattr(Weekday('tue', '', 1), 'square'))
        self.assertTrue(hasattr(Weekday('wed', '', 1), 'square'))
        self.assertFalse(hasattr(Weekday('thu', '', 1), 'square'))
        self.assertFalse(hasattr(Weekday('fri', '', 1), 'square'))

    def test_double_days_attr(self):
        self.assertFalse(hasattr(Weekday('mon', '', 1), 'double'))
        self.assertFalse(hasattr(Weekday('tue', '', 1), 'double'))
        self.assertFalse(hasattr(Weekday('wed', '', 1), 'double'))
        self.assertTrue(hasattr(Weekday('thu', '', 1), 'double'))
        self.assertTrue(hasattr(Weekday('fri', '', 1), 'double'))

    def test_day_square_value(self):
        self.assertEqual(Weekday('mon', '', 1).square, 1)
        self.assertEqual(Weekday('mon', '', 3).square, 9)
        self.assertEqual(Weekday('mon', '', -1).square, 1)
        self.assertEqual(Weekday('mon', '', 0).square, 0)

    def test_day_double_value(self):
        self.assertEqual(Weekday('thu', '', 1).double, 2)
        self.assertEqual(Weekday('thu', '', 3).double, 6)
        self.assertEqual(Weekday('thu', '', -1).double, -2)
        self.assertEqual(Weekday('thu', '', 0).double, 0)

    def test_day_description_concatenation(self):
        self.assertEqual(Weekday('mon', 'test', 3).description, 'test 9')
        self.assertEqual(Weekday('fri', 'test', 3).description, 'test 6')

    def test_string_output_order(self):
        self.assertEqual(Weekday('mon', 'test', 1).__str__(),
                         '{"day": "mon", "description": "test 1", "square": 1, "value": 1}')

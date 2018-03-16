import unittest
from unittest import mock
from pandas import DataFrame
from weekday_parser import WeekdayParser


class TestWeekdayParser(unittest.TestCase):

    def test_handles_missing_dir_or_no_csv_file_found(self):
        WeekdayParser('unknown')
        WeekdayParser('tests')

    @mock.patch('weekday_parser.WeekdayParser.output')
    def test_finds_all_csv_files(self, ou):
        WeekdayParser("csv")
        self.assertEqual(len(ou.mock_calls), 3, "expect three csv files in given directory")

    @mock.patch('weekday_parser.WeekdayParser.__init__')
    def test_process_data_data_frame(self, initial):
        initial.return_value = None
        results = WeekdayParser("").process_data(DataFrame(
            {"mon": 1, "description": "first_desc"}, index=[0]))
        self.assertEqual(str(results[0]),
                         '{"day": "mon", "description": "first_desc 1", "square": 1, "value": 1}')

    @mock.patch('weekday_parser.WeekdayParser.__init__')
    def test_process_day_range(self, initial):
        initial.return_value = None
        results = WeekdayParser("").process_data(DataFrame(
            {"mon-fri": 1, "description": "first_desc"}, index=[0]))
        self.assertEqual(len(results), 5)

    @mock.patch('weekday_parser.WeekdayParser.__init__')
    @mock.patch('weekday_parser.WeekdayParser.DAY_NAMES', ['a', 'b', 'c'])
    @mock.patch('weekday_parser.WeekdayParser.DAY_INDEX', {'a': 0, 'b': 1, 'c': 2})
    def test_day_range(self, initial):
        initial.return_value = None
        results = WeekdayParser("").weekdays_between('a', 'c')
        self.assertEqual(results, ['a', 'b',  'c'])

import glob
import os
import pandas
import json
from weekday import Weekday
import argparse


class WeekdayParser:
    """ WeekdayParser class to parse Comma Separated Values (csv) files found in given 'root' directory"""

    DAY_NAMES = ['mon', 'tue', 'wed', 'thu', 'fri']
    DAY_INDEX = {d: n for n, d in enumerate(DAY_NAMES)}
    CSV_TYPES = '*.csv'

    def __init__(self, root):
        for path in glob.glob(os.path.join(root, self.CSV_TYPES)):
            self.output(os.path.basename(path), self.process_data(pandas.read_csv(path)))

    def process_data(self, data):
        weekdays = []
        for name, values in data.iteritems():
            if name in self.DAY_NAMES:
                weekdays.append(Weekday(name, data.description.values[0], int(values[0])))
            else:
                day_range = list(filter(lambda element: element in name, self.DAY_NAMES))
                if len(day_range) > 1:
                    for day in self.weekdays_between(day_range[0], day_range[1]):
                        weekdays.append(Weekday(day, data.description.values[0], int(values[0])))
        return weekdays

    def weekdays_between(self, s, e):
        s, e = self.DAY_INDEX[s], self.DAY_INDEX[e]
        return [self.DAY_NAMES[n % 5] for n in range(s, e + (1 if e > s else 6))]

    @staticmethod
    def output(filename, results):
        print('{}\n{}'.format(filename, json.dumps([ob.__dict__ for ob in results])))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="""Extract data from valid weekly data CSV files""")
    parser.add_argument('-d', '--dir', type=str, default='csv', help='Set csv directory')
    argparse.ArgumentParser(description='Parses data from CSV files')
    args = parser.parse_args()
    WeekdayParser(args.dir)


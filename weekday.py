import json


class Weekday:
    """ Weekday class to define weekday data. init applies specific calculation using 'value' creating new
        attribute either 'square' or 'double' depending on 'day'.  The calculated value is appended to 'description'"""

    SQUARE_DAYS = ['mon', 'tue', 'wed']

    def __init__(self, day, description, value):
        self.day = day
        self.value = value
        if self.day in self.SQUARE_DAYS:
            self.square = self.value ** 2
            self.description = "{} {}".format(description, self.square)
        else:
            self.double = self.value * 2
            self.description = "{} {}".format(description, self.double)

    def __str__(self):
        return json.dumps(self.__dict__, sort_keys=True)

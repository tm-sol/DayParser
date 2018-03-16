# Day Parser

### Pre-requisites:
* Python 3.x
* Pip

## Installation
$ pip install -r requirements.txt

#### Running Application

Optional argument to change directory to for the CSV files can be supplied as detailed below.
If none is supplied then the application will default to 'csv'

```
python weekday_parser.py

or

python weekday_parser.py -d csv
```

#### Running Tests

```
python -m unittest discover -s tests
```
Tests are under the 'tests' package and methods of the TestCase classes must be prefixed with 'test_' to be auto-discovered by the unittest module.


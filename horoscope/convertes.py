from datetime import datetime


class YearConverter:
    regex = r"[0-9]{4}"

    def to_python(self, value):
        return int(value)

    def to_url(self, value):
        return str(value)


class MyFloatConverter:
    regex = r"[+-]?\d*\.\d+"

    def to_python(self, value):
        return float(value)

    def to_url(self, value):
        return str(value)


class MyDateConverter:
    regex = r"(0\d|1[0-2])-([0-2]\d|3[01])-(\d{4})"

    def to_python(self, value):
        return datetime.strptime(value, '%d-%m-%Y')

    def to_url(self, value):
        return datetime.strftime('%d-%m-%Y', value)


class SplitConvertor:
    regex = r'(\w+,)+\w+'

    def to_python(self, value):
        return value.split(",")

    def to_url(self, value):
        return ",".join(value)

class UpperConvertor:
    regex = r'\w+'

    def to_python(self, value):
        return value.upper()

    def to_url(self, value):
        return value
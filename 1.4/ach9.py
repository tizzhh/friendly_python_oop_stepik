import sys

lst_in = list(map(str.strip, sys.stdin.readlines()))


class DataBase:
    lst_data = []
    FIELDS = ('id', 'name', 'old', 'salary')

    def insert(self, data):
        for row in data:
            val = row.split()
            self.lst_data.append(dict(zip(self.FIELDS, val)))

    def select(self, a, b):
        return self.lst_data[a : b + 1]


db = DataBase()
db.insert(lst_in)

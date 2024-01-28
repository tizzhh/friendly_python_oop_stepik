import sys
from typing import Dict, List, Union


class Record:
    _pk = 0

    def __init__(self, fio: str, descr: str, old: int) -> None:
        self.__class__._pk += 1
        self.pk = self._pk
        self.fio = fio
        self.descr = descr
        self.old = int(old)

    def __hash__(self) -> int:
        return hash((self.fio.lower(), self.old))

    def __eq__(self, other: object) -> bool:
        return hash(self) == hash(other)


class DataBase:
    def __init__(self, path: str = '') -> None:
        self.path = path
        self.dict_db: Dict[Record, List[Record]] = {}

    def write(self, record: Record) -> None:
        self.dict_db[record] = self.dict_db.get(record, []) + [record]

    def read(self, pk: int) -> Union[Record, None]:
        for record in self.dict_db:
            if record._pk == pk:
                return record


lst_in = list(map(str.strip, sys.stdin.readlines()))
lst_in2 = [string.split('; ') for string in lst_in]
db = DataBase()
for data in lst_in2:
    db.write(Record(*data))

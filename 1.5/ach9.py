import sys

class ListObject:
    def __init__(self, data) -> None:
        self.next_obj = None
        self.data = data
    
    def link(self, obj):
        self.next_obj = obj

lst_in = list(map(str.strip, sys.stdin.readlines()))

objs = [ListObject(elem) for elem in lst_in]
for index, obj in enumerate(objs[:-1]):
    obj.next_obj = objs[index + 1]

head_obj = objs[0]
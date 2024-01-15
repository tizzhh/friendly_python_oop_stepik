class Goods:
    def __init__(self, name, price) -> None:
        self.name = name
        self.price = price

    def __str__(self) -> str:
        return f'{self.name}: {self.price}'


class Table(Goods):
    ...

class TV(Goods):
    ...

class Notebook(Goods):
    ...

class Cup(Goods):
    ...

class Cart:
    def __init__(self) -> None:
        self.goods = []

    def add(self, gd):
        self.goods.append(gd)

    def remove(self, indx):
        self.goods.pop(indx)

    def get_list(self):
        return [
            str(gd) for gd in self.goods
        ]
    
cart = Cart()
tv1 = TV("samsung", 1111)
tv2 = TV("LG", 1234)
table = Table("ikea", 2345)
n1= Notebook("msi", 5433)
n2 = Notebook("apple", 542)
c = Cup("keepcup", 43)

cart.add(tv1)
cart.add(tv2)
cart.add(table)
cart.add(n1)
cart.add(n2)
cart.add(c)
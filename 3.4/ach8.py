from typing import Union


class Item:
    def __init__(self, name: str, money: Union[int, float]) -> None:
        self.name = name
        self.money = money

    def __add__(self, other) -> Union[int, float]:
        return self.money + other

    def __radd__(self, other) -> Union[int, float]:
        return self + other


class Budget:
    def __init__(self) -> None:
        self.items = []

    def add_item(self, it: Item) -> None:
        self.items.append(it)

    def remove_item(self, indx: int) -> None:
        if 0 <= indx <= len(self.items):
            self.items.pop(indx)

    def get_items(self) -> list[Item]:
        return self.items


my_budget = Budget()
my_budget.add_item(Item("Курс по Python ООП", 2000))
my_budget.add_item(Item("Курс по Django", 5000.01))
my_budget.add_item(Item("Курс по NumPy", 0))
my_budget.add_item(Item("Курс по C++", 1500.10))

# вычисление общих расходов
s = 0
for x in my_budget.get_items():
    s = s + x
print(s)

class Ingredient:
    def __init__(self, name: str, volume: float, measure: str) -> None:
        self.name = name
        self.volume = volume
        self.measure = measure

    def __str__(self) -> str:
        return f'{self.name}: {self.volume}, {self.measure}'


class Recipe:
    def __init__(self, *args) -> None:
        self.ingredients = list(args)

    def __len__(self) -> int:
        return len(self.ingredients)

    def add_ingredient(self, ing: Ingredient) -> None:
        self.ingredients.append(ing)

    def remove_ingredient(self, ing: Ingredient) -> None:
        self.ingredients.remove(ing)

    def get_ingredients(self) -> tuple[Ingredient]:
        return tuple(self.ingredients)


recipe = Recipe()
recipe.add_ingredient(Ingredient("Соль", 1, "столовая ложка"))
recipe.add_ingredient(Ingredient("Мука", 1, "кг"))
recipe.add_ingredient(Ingredient("Мясо баранины", 10, "кг"))
ings = recipe.get_ingredients()
n = len(recipe)  # n = 3

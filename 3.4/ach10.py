from typing import List, Union


class MaxPooling:
    def __init__(self, step: tuple, size: tuple) -> None:
        self.step = step
        self.size = size

    def __call__(
        self, matrix: List[List[Union[int, float]]]
    ) -> List[List[Union[int, float]]]:
        self.check_matrix(matrix)
        res = []

        for i in range(0, len(matrix), self.step[0]):
            one_row = []
            for j in range(0, len(matrix), self.step[1]):
                window = [
                    row[j : (j + 1) * self.size[1]]
                    for row in matrix[i : (i + 1) * self.size[0]]
                ]
                if self.check_if_skip(window):
                    continue
                one_row.append(self.find_max(window))
            if one_row:
                res.append(one_row)
        return res

    def check_if_skip(self, matrix: List[List[Union[int, float]]]) -> bool:
        if len(matrix) != self.size[0] or not all(
            len(row) == self.size[1] for row in matrix
        ):
            return True
        return False

    @staticmethod
    def find_max(matrix: List[List[Union[int, float]]]) -> int:
        return max([max(row) for row in matrix])

    @staticmethod
    def check_matrix(matrix: List[List[Union[int, float]]]):
        if [len(matrix)] * len(matrix) != [len(row) for row in matrix]:
            raise ValueError("Неверный формат для первого параметра matrix.")
        for row in matrix:
            for col in row:
                if not isinstance(col, (int, float)) or isinstance(col, bool):
                    raise ValueError(
                        "Неверный формат для первого параметра matrix."
                    )


# mp = MaxPooling(step=(2, 2), size=(2,2))
# res = mp([[1, 2, 3, 4], [5, 6, 7, 8], [9, 8, 7, 6], [5, 4, 3, 2]])    # [[6, 8], [9, 7]]
# print(res)
mp = MaxPooling(step=(2, 2), size=(2, 2))
m1 = [[1, 10, 10], [5, 10, 0], [0, 1, 2]]
m2 = [[1, 10, 10, 12], [5, 10, 0, -5], [0, 1, 2, 300], [40, -100, 0, 54.5]]
res1 = mp(m1)
res2 = mp(m2)
# print(res1)
assert res1 == [[10]], "неверный результат операции MaxPooling"
assert res2 == [[10, 12], [40, 300]], "неверный результат операции MaxPooling"

mp = MaxPooling(step=(3, 3), size=(2, 2))
m3 = [[1, 12, 14, 12], [5, 10, 0, -5], [0, 1, 2, 300], [40, -100, 0, 54.5]]
res3 = mp(m3)
assert res3 == [
    [12]
], "неверный результат операции при MaxPooling(step=(3, 3), size=(2,2))"
try:
    res = mp([[1, 2], [3, 4, 5]])
except ValueError:
    assert True
else:
    assert (
        False
    ), "некорректо отработала проверка (или она отсутствует) на не прямоугольную матрицу"

try:
    res = mp([[1, 2], [3, '4']])
except ValueError:
    assert True
else:
    assert (
        False
    ), "некорректо отработала проверка (или она отсутствует) на не числовые значения в матрице"


mp = MaxPooling(step=(1, 1), size=(5, 5))
res = mp(
    [
        [5, 0, 88, 2, 7, 65],
        [1, 33, 7, 45, 0, 1],
        [54, 8, 2, 38, 22, 7],
        [73, 23, 6, 1, 15, 0],
        [4, 12, 9, 1, 76, 6],
        [0, 15, 10, 8, 11, 78],
    ]
)  # [[88, 88], [76, 78]]

assert res == [
    [88, 88],
    [76, 78],
], "неверный результат операции MaxPooling(step=(1, 1), size=(5, 5))"

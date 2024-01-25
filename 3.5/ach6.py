from typing import Tuple


class Morph:
    def __init__(self, *args) -> None:
        self.morphs = list([word.lower() for word in args])

    def __eq__(self, other: str) -> bool:
        return other.lower() in self.morphs

    def add_word(self, word: str) -> None:
        if word not in self.morphs:
            self.morphs.append(word)

    def get_words(self) -> Tuple[str, ...]:
        return tuple(self.morphs)


dict_words = [
    Morph(
        'связь',
        'связи',
        'связью',
        'связи',
        'связей',
        'связям',
        'связями',
        'связях',
    ),
    Morph(
        'формула',
        'формулы',
        'формуле',
        'формулу',
        'формулой',
        'формул',
        'формулам',
        'формулами',
        'формулах',
    ),
    Morph(
        'вектор',
        'вектора',
        'вектору',
        'вектором',
        'векторе',
        'векторы',
        'векторов',
        'векторам',
        'векторами',
        'векторах',
    ),
    Morph(
        'эффект',
        'эффекта',
        'эффекту',
        'эффектом',
        'эффекте',
        'эффекты',
        'эффектов',
        'эффектам',
        'эффектами',
        'эффектах',
    ),
    Morph('день', 'дня', 'дню', 'днем', 'дне', 'дни', 'дням', 'днями', 'днях'),
]
text = [word.lower().strip('.,?!;') for word in input().split()]

count = 0
for word in text:
    for morph in dict_words:
        if word == morph:
            count += 1
            break
print(count)

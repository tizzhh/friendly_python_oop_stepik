class StringText:
    def __init__(self, lst_words) -> None:
        self.lst_words = lst_words

    def __lt__(self, other) -> bool:
        return len(self) < len(other)

    def __le__(self, other) -> bool:
        return len(self) <= len(other)

    def __len__(self) -> int:
        return len(self.lst_words)


stich = [
    "Я к вам пишу – чего же боле?",
    "Что я могу еще сказать?",
    "Теперь, я знаю, в вашей воле",
    "Меня презреньем наказать.",
    "Но вы, к моей несчастной доле",
    "Хоть каплю жалости храня,",
    "Вы не оставите меня.",
]
lst_words = [
    [word.strip('–?!,.;') for word in string.split() if word.strip('–?!,.;')]
    for string in stich
]
lst_text = [StringText(string) for string in lst_words]
lst_text_sorted = sorted(lst_text, key=lambda x: len(x), reverse=True)
lst_text_sorted = [' '.join(string.lst_words) for string in lst_text_sorted]
print(lst_text_sorted)

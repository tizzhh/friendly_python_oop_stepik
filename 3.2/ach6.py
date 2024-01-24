class RenderList:
    def __init__(self, type_list: str) -> None:
        if type_list not in ['ul', 'ol']:
            self.type_list = 'ul'
        else:
            self.type_list = type_list

    def __call__(self, strings: list[str]) -> str:
        res = ''''''
        res += f'<{self.type_list}>'
        for string in strings:
            res += f'<li>{string}</li>'
        res += f'</{self.type_list}>'
        return res


lst = ["Пункт меню 1", "Пункт меню 2", "Пункт меню 3"]
render = RenderList("ol")
html = render(lst)
print(html)

from typing import Callable


class HandlerGET:
    def __init__(self, func: Callable) -> None:
        self.__func = func

    def __call__(self, request: dict[str, str], *args, **kwargs) -> str:
        return self.get(self.__func, request, *args, **kwargs)

    def get(self, func: Callable, request: dict[str, str], *args, **kwargs):
        if request.get('method', 'GET') == 'GET':
            return 'GET: ' + str(func(request))
        return None


@HandlerGET
def contact(request):
    return "Сергей Балакирев"


res = contact({"method": "GET", "url": "contact.html"})
print(res)

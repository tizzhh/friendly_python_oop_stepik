from typing import Callable, Union

# class Handler:
#     def __init__(self, methods: tuple[str] = ('GET',)) -> None:
#         self.__methods = methods

#     def __call__(self, func: Callable) -> Callabe:
#         def wrapper(request: dict[str, str], *args, **kwargs):
#             if (method := request.get('method', 'GET')) in self.__methods:
#                 return method + ' ' + str(func(request))
#         return wrapper


class Handler:
    def __init__(self, methods: tuple[str] = ('GET',)) -> None:
        self.__methods = methods

    def __call__(self, func: Callable) -> Callable:
        def wrapper(
            request: dict[str, str], *args, **kwargs
        ) -> Union[str, None]:
            method = request.get('method', 'GET')
            if method in self.__methods:
                if method == 'GET':
                    return self.get(func, request, *args, **kwargs)
                elif method == 'POST':
                    return self.post(func, request, *args, **kwargs)
                return None

        return wrapper

    def get(
        self, func: Callable, request: dict[str, str], *args, **kwargs
    ) -> str:
        return 'GET: ' + str(func(request))

    def post(
        self, func: Callable, request: dict[str, str], *args, **kwargs
    ) -> str:
        return 'POST: ' + str(func(request))


@Handler(methods=('GET', 'POST'))
def contact(request):
    return "Сергей Балакирев"


res = contact({"method": "POST", "url": "contact.html"})
print(res)

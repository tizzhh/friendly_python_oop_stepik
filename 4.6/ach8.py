from typing import Dict


class RetriveMixin:
    def get(self, request):
        return "GET: " + request.get('url')


class CreateMixin:
    def post(self, request):
        return "POST: " + request.get('url')


class UpdateMixin:
    def put(self, request):
        return "PUT: " + request.get('url')


class GeneralView:
    allowed_methods = ('GET', 'POST', 'PUT', 'DELETE')

    def render_request(self, request: Dict[str, str]):
        if not request['method'] in self.allowed_methods:
            raise TypeError(f"Метод {request.get('method')} не разрешен.")
        method_request = request.get('method').lower()
        return super().__getattribute__(method_request)(request)


class DetailView(RetriveMixin, UpdateMixin, GeneralView):
    allowed_methods = (
        'GET',
        'PUT',
    )


view = DetailView()
html = view.render_request(
    {'url': 'https://stepik.org/course/116336/', 'method': 'PUT'}
)
print(html)

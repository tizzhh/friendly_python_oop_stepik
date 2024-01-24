from typing import Any


class ImageFileAcceptor:
    def __init__(self, extensions: tuple[str]) -> None:
        self.extentions = extensions

    def __call__(self, file: str) -> bool:
        # if file.endswith(self.extentions)
        if file[file.rfind('.') + 1 :] in self.extentions:
            return True


filenames = [
    "boat.jpg",
    "web.png",
    "text.txt",
    "python.doc",
    "ava.8.jpg",
    "forest.jpeg",
    "eq_1.png",
    "eq_2.png",
    "my.html",
    "data.shtml",
]
acceptor = ImageFileAcceptor(('jpg', 'bmp', 'jpeg'))
image_filenames = filter(acceptor, filenames)
print(list(image_filenames))

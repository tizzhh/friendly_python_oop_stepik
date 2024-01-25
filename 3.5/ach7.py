from typing import Self


class FileAcceptor:
    def __init__(self, *args) -> None:
        self.exts = list(args)

    def __call__(self, filename: str) -> bool:
        return filename[filename.rfind('.') + 1 :] in self.exts

    def __add__(self, other: Self) -> Self:
        return self.__class__(*(set(self.exts) | set(other.exts)))


filenames = [
    "boat.jpg",
    "ans.web.png",
    "text.txt",
    "www.python.doc",
    "my.ava.jpg",
    "forest.jpeg",
    "eq_1.png",
    "eq_2.xls",
]
acceptor_images = FileAcceptor("jpg", "jpeg", "png")
acceptor_docs = FileAcceptor("txt", "doc", "xls")
filenames = list(filter(acceptor_images + acceptor_docs, filenames))
print(filenames)

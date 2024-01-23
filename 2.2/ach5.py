class WindowDlg:
    def __init__(self, title, width, height) -> None:
        self.__title = title
        self.__width = width
        self.__height = height

    @staticmethod
    def check_data(func):
        def wrapper(var):
            if isinstance(var, int) and 0 <= var <= 10000:
                return func(var)
            return wrapper

    def show(self):
        print(f'{self.__title}: {self.__width}, {self.__height}')

    @property
    def width(self):
        return self.__width

    @check_data
    @width.setter
    def width(self, width):
        self.__width = width
        self.show()

    @property
    def height(self):
        return self.__height

    @check_data
    @height.setter
    def height(self, height):
        self.__height = height
        self.show()


test = WindowDlg('a', 1, 2)
test.width = 10
print(test.width)

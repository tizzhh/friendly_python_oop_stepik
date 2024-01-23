class TreeObj:
    def __init__(self, indx, value=None) -> None:
        self.indx = indx
        self.value = value
        self.__left = None
        self.__right = None

    @property
    def left(self):
        return self.__left

    @left.setter
    def left(self, left):
        self.__left = left

    @property
    def right(self):
        return self.__right

    @right.setter
    def right(self, right):
        self.__right = right


class DecisionTree:
    @classmethod
    def predict(cls, root: TreeObj, x: list):
        pointer = root
        res = None
        while pointer is not None:
            if pointer is not None:
                res = pointer.value
            pointer = pointer.left if x[pointer.indx] else pointer.right
        return res

    @classmethod
    def add_obj(
        cls, obj, node: TreeObj = None, left: TreeObj = True
    ) -> TreeObj:
        if node is None:
            cls.root = obj
            return cls.root
        else:
            if left:
                node.left = obj
                return node.left
            else:
                node.right = obj
                return node.right

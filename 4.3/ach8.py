class SoftList(list):
    def __getitem__(self, index):
        if abs(index) >= len(self):
            return False
        return super().__getitem__(index)


sl = SoftList("python")
print(sl[0])  # 'p'
print(sl[-1])  # 'n'
sl[6]  # False
sl[-7]  # False

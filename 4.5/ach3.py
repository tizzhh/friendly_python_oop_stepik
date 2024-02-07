class Student:
    def __init__(self, fio, group):
        self._fio = fio
        self._group = group
        self._lect_marks = []
        self._house_marks = []

    def add_lect_marks(self, mark):
        self._lect_marks.append(mark)

    def add_house_marks(self, mark):
        self._house_marks.append(mark)

    def __str__(self):
        return f"Студент {self._fio}: оценки на лекциях: {str(self._lect_marks)}; оценки за д/з: {str(self._house_marks)}"


class Mentor:
    def __init__(self, fio, subject):
        self._fio = fio
        self._subject = subject


class Lector(Mentor):
    def set_mark(self, student: Student, mark):
        student.add_lect_marks(mark)

    def __str__(self) -> str:
        return f'Лектор {self._fio}: предмет {self._subject}'


class Reviewer(Mentor):
    def set_mark(self, student: Student, mark):
        student.add_house_marks(mark)

    def __str__(self) -> str:
        return f'Эксперт {self._fio}: предмет {self._subject}'

from lab_python_oop.color import Color
from lab_python_oop.figure import Figure
from lab_python_oop.rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, side: float, color: Color):
        super().__init__(side, side, color)
        self._name = "Квадрат"

    def __repr__(self):
        return "{}: сторона: {}, цвет: {}".format(self._name, self.width, self.color)

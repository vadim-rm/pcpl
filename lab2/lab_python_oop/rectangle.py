from lab_python_oop.color import Color
from lab_python_oop.figure import Figure


class Rectangle(Figure):
    def __init__(self, width: float, height: float, color: Color):
        self._name = "Прямоугольник"
        self.width = width
        self.height = height
        self.color = color

    def get_area(self) -> float:
        return self.height * self.width

    def __repr__(self):
        return "{}: ширина: {}, высота: {}, цвет: {}".format(self._name, self.width, self.height, self.color)

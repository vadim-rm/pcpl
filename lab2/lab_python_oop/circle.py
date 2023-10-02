import math

from lab_python_oop.color import Color
from lab_python_oop.figure import Figure


class Circle(Figure):
    def __init__(self, radius: float, color: Color):
        self._name = "Круг"
        self._radius = radius
        self._color = color

    def get_area(self) -> float:
        return self._radius * math.pi

    def __repr__(self):
        return "{}: радиус: {}, цвет: {}".format(self._name, self._radius, self._color)

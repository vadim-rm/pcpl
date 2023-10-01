import sys
from typing import Optional, Callable

from entity.coefficients import Coefficients
from entity.exceptions import WrongInput


class InputService:
    @staticmethod
    def parse_float_from_string(inp: str, validator: Optional[Callable[[float], bool]] = None) -> float:
        digit = float(inp)
        if validator and not validator(digit):
            raise ValueError()

        return digit

    def get_float_from_terminal(self, prompt: str, validator: Optional[Callable[[float], bool]] = None) -> float:
        while True:
            try:
                print(prompt)
                inp = input()

                return self.parse_float_from_string(inp, validator)
            except ValueError:
                print("Неверный ввод")

    def get_coefficients(self) -> Coefficients:
        if len(sys.argv) < 3:
            a = self.get_float_from_terminal("Введите коэффициент A", lambda x: x != 0)
            b = self.get_float_from_terminal("Введите коэффициент B")
            c = self.get_float_from_terminal("Введите коэффициент C")
        else:
            try:
                args = sys.argv[1:]
                a = self.parse_float_from_string(args[0], lambda x: x != 0)
                b = self.parse_float_from_string(args[1])
                c = self.parse_float_from_string(args[2])
            except ValueError:
                raise WrongInput()

        return Coefficients(
            A=a,
            B=b,
            C=c,
        )

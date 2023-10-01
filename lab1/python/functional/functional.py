import sys
from dataclasses import dataclass
from math import sqrt
from typing import Callable, Optional, Set


class WrongInput(Exception):
    pass


class NoSolutions(Exception):
    pass


@dataclass
class Coefficients:
    A: float
    B: float
    C: float


def parse_float_from_string(inp: str, validator: Optional[Callable[[float], bool]] = None) -> float:
    digit = float(inp)
    if validator and not validator(digit):
        raise ValueError()

    return digit


def get_float_from_terminal(prompt: str, validator: Optional[Callable[[float], bool]] = None) -> float:
    while True:
        try:
            print(prompt)
            inp = input()

            return parse_float_from_string(inp, validator)
        except ValueError:
            print("Неверный ввод")


def get_coefficients() -> Coefficients:
    if len(sys.argv) < 3:
        a = get_float_from_terminal("Введите коэффициент A", lambda x: x != 0)
        b = get_float_from_terminal("Введите коэффициент B")
        c = get_float_from_terminal("Введите коэффициент C")
    else:
        try:
            args = sys.argv[1:]
            a = parse_float_from_string(args[0], lambda x: x != 0)
            b = parse_float_from_string(args[1])
            c = parse_float_from_string(args[2])
        except ValueError:
            print("Неверные аргументы командной строки")
            exit()

    return Coefficients(
        A=a,
        B=b,
        C=c,
    )


def solve(coefficients: Coefficients) -> Set[float]:
    d = coefficients.B ** 2 - 4 * coefficients.A * coefficients.C
    if d < 0:
        raise NoSolutions()
    roots: Set[float] = set()

    possible_roots = [
        (-coefficients.B - sqrt(d)) / (2 * coefficients.A),
        (-coefficients.B + sqrt(d)) / (2 * coefficients.A),
    ]

    for root in possible_roots:
        if root >= 0:
            roots.add(sqrt(root))
            roots.add(-sqrt(root))

    return roots


if __name__ == "__main__":
    coefficients = get_coefficients()
    try:
        print(solve(coefficients))
    except NoSolutions:
        print("Нет решений")

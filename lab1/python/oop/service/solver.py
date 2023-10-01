from math import sqrt
from typing import Set

from entity.coefficients import Coefficients
from entity.exceptions import NoSolutions


class SolverService:
    @staticmethod
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

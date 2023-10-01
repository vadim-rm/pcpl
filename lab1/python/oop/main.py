from entity.exceptions import WrongInput, NoSolutions
from service.input import InputService
from service.solver import SolverService

if __name__ == "__main__":
    solver_service = SolverService()
    input_service = InputService()
    try:
        coefficients = input_service.get_coefficients()
        print(solver_service.solve(coefficients))
    except WrongInput:
        print("Неверный ввод")
    except NoSolutions:
        print("Нет решений")

from abc import abstractmethod, ABCMeta


class Figure(metaclass=ABCMeta):
    @abstractmethod
    def get_area(self) -> float:
        pass

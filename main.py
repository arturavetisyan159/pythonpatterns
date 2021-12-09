# Паттерны проектирования
from abc import abstractmethod, ABC

class Logistics(ABC):
    @abstractmethod
    def create_transport(self):
        pass

# class




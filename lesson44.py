# Паттерн "Стратегия"

# Dyson V11

class VacuumCleaner:
    def __init__(self):
        self.clean_strategy = PlitkaStrategy()
        self.friction = 0

    def check_strategy(self):
        if self.friction <= 5:
            self.clean_strategy = PlitkaStrategy
        elif 5 < self.friction < 10:
            self.clean_strategy = PalaceStrategy()
        elif self.friction > 10:
            self.clean_strategy = CoverStrategy()

    def clean(self):
        self.check_strategy()
        self.clean_strategy.clean()


class ICleanStrategy:
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def clean(self):
        pass


class CoverStrategy(ICleanStrategy):
    def __init__(self):
        super().__init__("ковер", 10)

    def clean(self):
        print(f"Тип поверхности: {self.name} | мощность: {self.power} ")


class PlitkaStrategy(ICleanStrategy):
    def __init__(self):
        super().__init__("плитка", 5)

    def clean(self):
        print(f"Тип поверхности: {self.name} | мощность: {self.power} ")


class PalaceStrategy(ICleanStrategy):
    def __init__(self):
        super().__init__("палас", 8)

    def clean(self):
        print(f"Тип поверхности: {self.name} | мощность: {self.power} ")


##############################

# SOLID
# S - Single Responsibility Principle (Принцип Единственной Ответственности)
# O - Open-Closed Principle (Принцип открытости-закрытости)
# L - Liskov Substitution Principle (Принцип подстановки Лискова)
# I - Interface Sigregation (Принцип раздедления интерфейса)
# D - Dependency Inversion Principle (Принцип Инверсии Зависимостей)


# S - Single Responsibility Principle (Принцип Единственной Ответственности)
# Одно поручение, всего одно. Каждый класс должен решать одну задачу в рамках сущности, под которую этот класс создается

# class Animal:
#     def __init__(self, name):
#         self.name = name
#
#     def get_animal_name(self):
#         return self.name
#
#     def save_animal(self): # Ошибка. Это должно быть в другом классе реализовано.
#         pass


# O - Open-Closed Principle (Принцип открытости-закрытости)
# сущность открыта для расширения, закрыта для модификации.
# расширение имеется в виду наследование.

class Animal:
    def __init__(self, name):
        self.name = name

    def get_animal_name(self):
        return self.name

    def make_sound(self):
        pass

class Cat(Animal):
    def __init__(self, name="cat"):
        super().__init__(name)

    def make_sound(self):
        print("Meow")


class Dog(Animal):
    def __init__(self, name="dog"):
        super().__init__(name)

    def make_sound(self):
        print("Bark")


class Cow(Animal):
    def __init__(self, name="cow"):
        super().__init__(name)

    def make_sound(self):
        print("mooh")

animals = [Cat(), Dog(), Cow()]

def get_animal_name(animals: list[Animal]):
    for an in animals:
        an.make_sound()





def main():
    pass

if __name__ == "__main__":
    get_animal_name(animals)

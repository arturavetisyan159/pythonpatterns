from abc import ABC, abstractmethod
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

# class Animal:
#     def __init__(self, name):
#         self.name = name
#
#     def get_animal_name(self):
#         return self.name
#
#     def make_sound(self):
#         pass
#
# class Cat(Animal):
#     def __init__(self, name="cat"):
#         super().__init__(name)
#
#     def make_sound(self):
#         print("Meow")
#
#
# class Dog(Animal):
#     def __init__(self, name="dog"):
#         super().__init__(name)
#
#     def make_sound(self):
#         print("Bark")
#
#
# class Cow(Animal):
#     def __init__(self, name="cow"):
#         super().__init__(name)
#
#     def make_sound(self):
#         print("mooh")
#
# animals = [Cat(), Dog(), Cow()]
#
# def get_animal_name(animals: list[Animal]):
#     for an in animals:
#         an.make_sound()


# L - Liskov Substitution Principle (Принцип подстановки Лискова)
# необходимо, чтобы потомки служили заменой своим родителям.

# class Animal:
#     def __init__(self, name, legs):
#         self.name = name
#         self.legs = legs
#
#     def get_animal_legs(self): # один общий метод на все.
#         return self.legs
#
# class Cat(Animal):
#     def __init__(self, name="cat", legs=4):
#         super().__init__(name, legs)
#
#     def make_sound(self):
#         print("Meow")
#
#
# class Dog(Animal):
#     def __init__(self, name="dog", legs=4):
#         super().__init__(name, legs)
#
#     def make_sound(self):
#         print("Bark")
#
# animals = [Cat(), Dog()]


##########################
# I - Interface Sigregation (Принцип раздедления интерфейса)
# Создавайте узкоспециализированные интерфейсы, предназначенные для конкретного клиента. Клиенты не должн зависеть
# от интерфейсов, котрые они не используют


# class IFigure(ABC):
#     @abstractmethod
#     def draw(self):
#        pass
#
#
# class Circle(IFigure):
#     def draw(self):
#         print("draw circle")
#
#
# class Square(IFigure):
#     def draw(self):
#         print("draw square")
#
#
# class Rectangle(IFigure):
#     def draw(self):
#         print("draw rectangle")
#
#
# figures = [Circle(), Rectangle(), Square()]

###################
# D - Dependency Inversion Principle (Принцип Инверсии Зависимостей)
# Объектом зависимости должна быть абстракция, а не что то конкретное.
# Модули верхних модулей не должны зависеть от модулей нижних уровней. Оба типа модулей должны зависеть от абстракций.
# Абстракции не должны зависеть от деталей. Это детали должны зависеть от абстракций.

class ConsolePrinter:
    def print(self):
        pass

    def do_smth_with_internal_params1(self):
        pass

    def do_smth_with_internal_params2(self):
        pass

    def public_interface_with_internal_logic(self):
        a = self.printer.do_smth_with_internal_params1()
        b = self.printer.do_smth_with_internal_params2()
        c = a + b
        return c


class Book:
    def __init__(self):
        self.printer = ConsolePrinter()

    def print(self):
        a = self.printer.public_interface_with_internal_logic()
        return a

def main():
    pass

if __name__ == "__main__":
    main()

import doctest

# Тестирование кода

# def func(a, b):
#     """
#     Функция, складывающая 2 числа.
#
#     >>> func(1,2)
#     4
#     """
#     return a + b

def factorial(n):
    if n < 2:
        return 1
    return n * factorial(n-1)

class Calculator:
    def add(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b

    def mul(self, a, b):
        return a * b

    def div(self, a, b):
        return a / b

def main():
    # doctest.testmod()
    print(factorial(5))

if __name__ == "__main__":
    main()

import unittest
import sys
from lesson46 import factorial, Calculator

# class TestFactorial(unittest.TestCase):
#     def test_func(self):
#         a = factorial(5)
#         self.assertEqual(a, 121, f'Переменная a != {a}')
#
#     def test_func2(self):
#         a = factorial(3)
#         self.assertEqual(a, 120)


class TestCalculator(unittest.TestCase):
    def setUp(self) -> None:
        # print(Создаю кальк)
        self.calc = Calculator()

    def tearDown(self) -> None:
        # print('Удаляю calc')
        del self.calc

    @unittest.skip('Не хочу тестировать сложение ')
    def test_add(self):
        result = self.calc.add(4, 5)
        self.assertEqual(result, 9)

    def test_sub(self):
        result = self.calc.sub(4, 5)
        self.assertEqual(result, -1)

    def test_mul(self):
        result = self.calc.mul(4, 5)
        self.assertEqual(result, 20)

    @unittest.expectedFailure
    def test_div(self):
        result = self.calc.div(4, 5)
        self.assertEqual(result, 0.8)

if __name__ == "__main__":
    unittest.main()


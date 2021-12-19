# MVC
# M(model), V(view), C(controller)
# Модель - это бизнес логика + данные (например БД).
# Вид - то, что видит пользователь.
# Контроллер - то, что обрабатывает пользовательский ввод.
from controller import *


def main():
    app = Controller()
    app.run()

if __name__ == "__main__":
    main()





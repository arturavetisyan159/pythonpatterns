# Параллельное программирование
# Используется в 2-ух сучаях: при ситуации когда надо увеличить производительноую мощность и при
# интерактивности.
# В параллельном программировании нас интересует делать несколько вещей в одно время.
# Кто такие акторы в параллельном программировании? У компьютера есть процессор, в нем есть ядра, на которые как раз
# таки и ложатся параллельные задачи
# Параллельное программирование состоит из трех больших частей:
# 1) Многопроцессность
# 2) Многопоточность
# 3) Ассинхронность (один процесс, один поток, но все работает параллельно)
"""
if задача_ввода_вывода:
    if долгий_ввод_вывод:
        Ассинхронность
    else:
        Многопоточность
else:
    Многопроцессность
"""

import multiprocessing
from time import sleep, time

def sleeper(sec):
    print(f"{multiprocessing.current_process().name}: Засыпаю на {sec} cекунд")
    sleep(sec)
    print(f"{multiprocessing.current_process().name}: Я проснулся после {sec} секунд сна")


X = 0

def increment():
    print(f"{multiprocessing.current_process().name}: Начал инкремент X...")
    global X
    for i in range(1000000):
        X += 1
    print(f"{multiprocessing.current_process().name}: Закончил инкремент X")


def main():
    # sec = 3
    # proc1 = multiprocessing.Process(target=sleeper, name="Процесс 1", args=(sec,))
    # proc2 = multiprocessing.Process(target=sleeper, name="Процесс 2", args=(sec,))

    proc1 = multiprocessing.Process(target=increment, name="Процесс 1")
    proc2 = multiprocessing.Process(target=increment, name="Процесс 2")

    start_time = time()

    proc1.start()
    proc2.start()

    proc1.join()
    proc2.join()

    end_time = time()
    print(f"Программа исполнялась {end_time - start_time} секунд")
    print(f"Глобальная переменная X = {X}")

if __name__ == "__main__":
    main()



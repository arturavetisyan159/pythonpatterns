import threading
import time
import random
from statistics import mean

MY_LIST = []

def func_1():
    global MY_LIST
    MY_LIST = [random.randint(1, 11) for i in range(100)]
    print(f"{threading.current_thread().name}: сгенерировала список - {MY_LIST}")


def func_2():
    global MY_LIST
    sum = 0
    for el in MY_LIST:
        sum = el + sum
    print(f"{threading.current_thread().name}: сумма элементов в списке = {sum}")
    return sum

def func_3():
    global MY_LIST
    avg = mean(MY_LIST)
    print(f"{threading.current_thread().name}: среднее значение в списке = {avg}")


def main():
    thread_1 = threading.Thread(target=func_1, name="Поток 1")
    thread_2 = threading.Thread(target=func_2, name="Поток 2")
    thread_3 = threading.Thread(target=func_3, name="Поток 3")

    # thread_1.start()
    # thread_2.start()
    # thread_3.start()
    # thread_1.join()
    # thread_2.join()
    # thread_3.join()

    thread_1.start()
    thread_1.join()
    thread_2.start()
    thread_2.join()
    thread_3.start()
    thread_3.join()


if __name__ == "__main__":
    main()
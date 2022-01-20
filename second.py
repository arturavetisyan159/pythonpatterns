import threading
import time
import random
import sympy

def fac(n):
    if n == 0:
        return 1
    return fac(n-1) * n

def write(file_name):
    rand_list = [random.randint(1, 50) for i in range(50)]
    with open(file_name, "w", encoding="utf-8") as f:
        value = ''
        for el in rand_list:
            value += str(el) + ' '
        f.write(value)
    print(f"{threading.current_thread().name}: Сформировал файл из {len(rand_list)} элементов и записал в {file_name}")


def find_prime(file_name):
    res = []
    with open(file_name, "r", encoding="utf-8") as f:
        els = list(map(int, f.read().split()))
    for el in els:
        if sympy.isprime(el):
            res.append(el)
    file2 = "file2.txt"
    with open(file2, "w", encoding="utf-8") as f:
        value = ''
        for el in res:
            value += str(el) + ' '
        f.write(value)
    print(f"{threading.current_thread().name}: нашел простые числа и записал их в файл {file2}")


def factorial(file_name):
    with open(file_name, "r", encoding="utf-8") as f:
        els = list(map(int, f.read().split()))
    file3 = "file3.txt"
    with open(file3, "w", encoding="utf-8") as f:
        value = ''
        for el in els:
            value += str(fac(el)) + ' '
        f.write(value)
    print(f"{threading.current_thread().name}: записал факториал каждого числа в {file3}")


def main():
    file_name = input("Введите название файла куда все запишется: ")
    thread_1 = threading.Thread(target=write, name="Поток 1", args=(file_name,))
    thread_2 = threading.Thread(target=find_prime, name="Поток 2", args=(file_name,))
    thread_3 = threading.Thread(target=factorial, name="Поток 3", args=(file_name,))

    thread_1.start()
    thread_1.join()
    thread_2.start()
    thread_2.join()
    thread_3.start()
    thread_3.join()


if __name__ == "__main__":
    main()


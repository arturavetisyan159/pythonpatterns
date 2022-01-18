import multiprocessing
from time import sleep, time


def read_list(spisok):
    result = []
    if multiprocessing.current_process().name == "Процесс 1":
        for el in spisok:
            if el % 2 != 0:
                result.append(el)
        with open ("file_1.txt", "w", encoding="utf-8") as f:
            f.write(f"{result}")
        print(f"{multiprocessing.current_process().name} отработала")
    else:
        for el in spisok:
            if el % 2 == 0:
                result.append(el)
        with open("file_2.txt", "w", encoding="utf-8") as f:
            f.write(f"{result}")
        print(f"{multiprocessing.current_process().name} отработала")

def main():
    spisok = [i for i in range(1, 100)]
    # proc1 = multiprocessing.Process(target=sleeper, name="Процесс 1", args=(sec,))
    # proc2 = multiprocessing.Process(target=sleeper, name="Процесс 2", args=(sec,))

    proc1 = multiprocessing.Process(target=read_list, name="Процесс 1", args=(spisok,))
    proc2 = multiprocessing.Process(target=read_list, name="Процесс 2", args=(spisok,))

    start_time = time()

    proc1.start()
    proc2.start()

    proc1.join()
    proc2.join()

    end_time = time()
    print(f"Программа исполнялась {end_time - start_time} секунд")

if __name__ == "__main__":
    main()




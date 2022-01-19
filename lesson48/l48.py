# Поток, в отличие от проуесса - это просто набор инструкций.
# В рамках процесса существует главная нить. Эта нить и есть поток. В каждом процессе есть один главный поток,
# который и кладется на процессорные ядра.
# Важно понимать отличие между процессом и потоком. Процесс - совокупность системных ресурсов которые были выделены
# для решения задачи. Потоки существуют в рамках какого то процесса. Поток это набор инструкций, высылаемых какому то
# процессу.
# процессу

import time
import threading


# def func1(n):
#     for i in range(n):
#         print(f'{threading.current_thread().name} > {i}')


class MyThread(threading.Thread):
    def __init__(self, iterations):
        self.iterations = iterations
        self.res = 0
        super().__init__()

    def run(self):
        print(f'{threading.current_thread().name} начал работу')
        res = 0
        for _ in range(self.iterations):
            res += 1
        print(f'{threading.current_thread().name} закончил работу | {res = }')
        self.res = res


X = 0
def increment(N):
    print(f'{threading.current_thread().name} начал работу')
    global X
    for _ in range(N):
        X += 1
    print(f'{threading.current_thread().name} закончил работу')

def main():
    N = 1_000_000_0
    print("Главный поток начал работу")

    thread1= threading.Thread(target=increment, name="Поток №1", args=(N,))
    thread2 = threading.Thread(target=increment, name="Поток №2", args=(N,))

    my_thread = MyThread(1000000)

    start_time = time.time()
    # thread1.start()
    # thread2.start()
    # thread1.join()
    # thread2.join()
    my_thread.start()
    my_thread.join()
    end_time = time.time()
    print(f"Главный поток закончил работу за {start_time - end_time} сек")
    print(f"{X = }")


if __name__ == "__main__":
    main()






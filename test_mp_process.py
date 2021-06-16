import multiprocessing
import random
import time
import os

NumOfConsumers = multiprocessing.cpu_count()

def consumer(jobs:multiprocessing.Queue, results:multiprocessing.Queue):
    while True:
        n = jobs.get()
        result = n * n
        results.put(result)
        jobs.task_done()

def producer(signal:multiprocessing.Queue):

    tasks = multiprocessing.JoinableQueue()
    results = multiprocessing.Queue()

    print('Creating {} consumers'.format(NumOfConsumers))
    square = lambda n: n*n
    for i in range(0, NumOfConsumers):
        process = multiprocessing.Process(target=consumer, args=(tasks, results))
        process.daemon = True # процесс завершится, если producer завершит работу
        process.start()

    # пока пользователь не закрыл программу
    while(signal.empty()):
        #randomlist = []
        s:str = "roots: "
        for i in range(0, NumOfConsumers):
            num = random.randint(1000, 9999)
            #randomlist.append(n)
            tasks.put(num)
            s += str(num) + ", "
        print(s)

        # ждем опустошения списка задач
        tasks.join()

        sum = 0
        for i in range(0, NumOfConsumers):
            # опустошить список. попутно считаем сумму
            sum += results.get()
        print("sum: ", str(sum))
    print("producer stopped")

if __name__ == '__main__':
    signal = multiprocessing.Queue()

    producer_ = multiprocessing.Process(target=producer, args=(signal, ))
    producer_.start()
    producer_.join()

    input('Press ENTER to exit...')
    signal.put(1)
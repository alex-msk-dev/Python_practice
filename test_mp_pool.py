import multiprocessing
import random
import time
import os

NumOfConsumer = multiprocessing.cpu_count()

def consumerFunc(x):
    return x*x
# есть один продюсер, , который генерирует запросы или числа
def producerFunc():

    with multiprocessing.Pool(processes=NumOfConsumer) as pool:
        randomlist = []
        for i in range(0, NumOfConsumer):
            n = random.randint(1000, 9999)
            randomlist.append(n)

        squareLst = pool.map(consumerFunc, randomlist)

        s:str = "roots: "
        for num in randomlist:
            s += str(num) + ", "
        print(s)

        sum = 0
        for square in squareLst:
            sum += square
        print("sum: ", str(sum))

    # exiting the 'with'-block has stopped the pool
    print("Now the pool is closed and no longer available")
    return

if __name__ == '__main__':
    queue = multiprocessing.Queue()
    producer = multiprocessing.Process(target=producerFunc, args=())
    producer.start()
    producer.join()
    input('Press ENTER to exit...')
import argparse
import matplotlib.pyplot as plt
import time

from SweepLineAlgorithm import *

def generate_lines(n):

    result = []

    x1 = 0
    y = 6
    x2 = 15

    for i in range(n):
        result.append((x1 + 0.1 * i, y - 0.1 * i , x2 + 0.1 * i, y - 0.1 * i, i + 1))

    return result

def test():

    avl_time = []
    b_2_3_time = []
    n = []

    for i in range(1, 1000):
        
        Lines = []

        number = i * 2

        data = generate_lines(number)
        for line in data:
            Lines.append(Line(line[0], line[1], line[2], line[3], line[4]))

        E = []

        for line in Lines:
            start, end = line.split()
            E.append(start)
            E.append(end)

        start = time.time() 
        sweep_line(E, 1)
        end = time.time() - start
        avl_time.append(end)

        start = time.time()
        sweep_line(E, 0)
        end = time.time() - start
        b_2_3_time.append(end)

        n.append(number)

    for elem in avl_time:
        print(elem)
    for elem in b_2_3_time:
        print(elem)        
    plt.plot(avl_time, n, label='avl')
    plt.plot(b_2_3_time, n, label='2-3')
    plt.legend(loc='best')
    plt.show()

if __name__ == "__main__":
    test()
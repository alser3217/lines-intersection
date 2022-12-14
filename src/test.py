import argparse
import matplotlib.pyplot as plt
import time
import random
from random import randrange
import math

from SweepLineAlgorithm import *

def experiment1(n, k=None):

    res = []

    if k:
        max = 0

        for i in range(k):

            x1  = random.uniform(0, 0.5)
            if x1 > max:
                max = x1
            y1  = random.random()

            offset = random.uniform(0.1, 0.5 - x1)
            x2  = random.uniform(x1, x1 + offset)
            res.append((x1, y1, x2, y1, i + 1))

        x2k1 = max + 0.2
        x2k2 = max + 0.22
        res.append((max + 0.1, 0.7, max + 0.2, 0.3, k + 1))
        res.append((max + 0.12, 0.3, max + 0.22, 0.7, k + 2))

        for i in range(n - k - 2):
            x1  = random.uniform(x2k2 + 0.1, 0.8)
            y1  = random.random()

            offset = random.uniform(0.1, 1 - x1)
            x2  = random.uniform(x1, x1 + offset)
            res.append((x1, y1, x2, y1, i + 1, n - k + 3 + i))

        return res
    else:

        for i in range(n):

            x1  = random.random()
            y1  = random.random()
            x2  = random.uniform(x1, 1)
            y2  = random.random()
            res.append((x1, y1, x2, y2, i + 1))

        return res

def experiment3(n):

    res = []
    r = 0.0001
    angle = random.uniform(0.1, math.pi / 2)

    for i in range(n):

        centerX = random.uniform(0.1, 0.9)
        centerY = random.uniform(0.1, 0.9)

        x1 = centerX - r/2 * math.cos(angle)
        y1 = centerY - r/2 * math.sin(angle)

        x2 = centerX + r/2 * math.cos(angle)
        y2 = centerY + r/2 * math.sin(angle)
        res.append((x1, y1, x2, y2, i + 1))

    return res

def experiment2(n, k):

    res = []
    max = 0

    for i in range(k):

        x1  = random.uniform(0, 0.5)
        if x1 > max:
            max = x1
        y1  = random.random()

        offset = random.uniform(0.1, 0.5 - x1)
        x2  = random.uniform(x1, x1 + offset)
        res.append((x1, y1, x2, y1, i + 1))

    x2k1 = max + 0.2
    x2k2 = max + 0.22
    res.append((max + 0.1, 0.7, max + 0.2, 0.3, k + 1))
    res.append((max + 0.12, 0.3, max + 0.22, 0.7, k + 2))

    for i in range(n - k - 2):
        x1  = random.uniform(x2k2 + 0.1, 0.8)
        y1  = random.random()

        offset = random.uniform(0.1, 1 - x1)
        x2  = random.uniform(x1, x1 + offset)
        res.append((x1, y1, x2, y1, i + 1, n - k + 3 + i))

    return res

def experiment4(n, r):

    res = []
    angle = random.uniform(0.1, math.pi / 2)

    for i in range(n):

        centerX = random.uniform(0.1, 0.9)
        centerY = random.uniform(0.1, 0.9)

        x1 = centerX - r/2 * math.cos(angle)
        y1 = centerY - r/2 * math.sin(angle)

        x2 = centerX + r/2 * math.cos(angle)
        y2 = centerY + r/2 * math.sin(angle)
        res.append((x1, y1, x2, y2, i + 1))

    return res

def test():

    parser = argparse.ArgumentParser(description='Process data')
    parser.add_argument('--experiment', type=int, default=1, metavar='P',
                        help='experiment number (default: 1)')

    args = parser.parse_args()

    avl_time = []
    b_2_3_time = []
    naive_time = []
    n = []

    length = []

    if args.experiment == 1:

        N = 10001
        step = 100

        for i in range(1, N, step):
            
            Lines = []
            number = i
            data = experiment1(number)
            
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

            start = time.time()
            sweep_line(E, 2, Lines)
            end = time.time() - start
            naive_time.append(end)

            n.append(number)    
        plt.plot(n, avl_time, label='avl')
        plt.plot(n, b_2_3_time, label='2-3')
        plt.plot(n, naive_time, label='naive')
        plt.legend(loc='best')
        plt.xlabel("N (количество отрезков)")
        plt.ylabel("Время (секунды)")
        plt.title("Experiment 1. N = 1...10001, step = 100")
        plt.show()     
  
    elif args.experiment == 2:

        N = 2000
        step = 100

        for i in range(1, N, step):

            number = i
            data = experiment1(N, i)

            Lines = []
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

            start = time.time()
            sweep_line(E, 2, Lines)
            end = time.time() - start
            naive_time.append(end)

            n.append(number)

        plt.plot(n, avl_time, label='avl')
        plt.plot(n, b_2_3_time, label='2-3')
        plt.plot(n, naive_time, label='naive')
        plt.legend(loc='best')
        plt.xlabel("k (количество первых непересекающихся отрезков)")
        plt.ylabel("Время (секунды)")
        plt.title("Experiment 2. N = 2000, k = 1...2000, step=100")
        plt.show()

    elif args.experiment == 3:

        N = 1000
        step = 100

        for i in range(1, N, step):

            number = i
            data = experiment3(number)

            Lines = []
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

            start = time.time()
            sweep_line(E, 2, Lines)
            end = time.time() - start
            naive_time.append(end)

            n.append(number)

        plt.plot(n, avl_time, label='avl')
        plt.plot(n, b_2_3_time, label='2-3')
        plt.plot(n, naive_time, label='naive')
        plt.legend(loc='best')
        plt.xlabel("N (количество отрезков)")
        plt.ylabel("Время (секунды)")
        plt.title("Experiment 3. N = 1...1000, step = 100, r = 0.0001")        
        plt.show()

    elif args.experiment == 4:

        N = 1000
        r = 0

        for i in range(1, 30):

            r += 0.001
            length.append(r)
            data = experiment4(N, r)

            Lines = []
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

            start = time.time()
            sweep_line(E, 2, Lines)
            end = time.time() - start
            naive_time.append(end)

        plt.plot(length, avl_time, label='avl')
        plt.plot(length, b_2_3_time, label='2-3')
        plt.plot(length, naive_time, label='naive')
        plt.legend(loc='best')
        plt.xlabel("r (длина отрезка)")
        plt.ylabel("Время (секунды)")
        plt.title("Experiment 4. N = 1000, r = 0.001...0.03, step = 0.001")          
        plt.show()        

if __name__ == "__main__":
    test()
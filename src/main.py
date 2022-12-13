import argparse
import matplotlib.pyplot as plt
import time

from SweepLineAlgorithm import *

def main():

    parser = argparse.ArgumentParser(description='Process data')
    parser.add_argument('--path', type=str, default='', metavar='P',
                        help='path to input file')
    parser.add_argument('--mode', type=int, default=1, metavar='M',
                        help='mode: 1 for AVL tree usage, 0 for 2-3 tree usage (default: 1)')

    args = parser.parse_args()

    Lines = []
    plot_data = []

    with open(args.path, 'r') as f:
        data = f.readlines()
        for line in data:
            tmp_arr = line.split()
            plot_data.append((tmp_arr[0], tmp_arr[2]))
            plot_data.append((tmp_arr[1], tmp_arr[3]))
            Lines.append(Line(float(tmp_arr[0]), float(tmp_arr[1]), float(tmp_arr[2]), float(tmp_arr[3]), tmp_arr[4]))
    for line in data: 
        Lines.append(Line(line[0], line[1], line[2], line[3], line[4]))
    
    E = []

    for line in Lines:
        start, end = line.split()
        E.append(start)
        E.append(end)

    start = time.time() 
    print(sweep_line(E, args.mode))
    end = time.time() - start

    print(f'Время выполнения: {end}')

if __name__ == "__main__":
    main()

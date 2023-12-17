import time
from collections import Counter
import re
import copy
from math import dist
import itertools
import sys
import cv2
import matplotlib.pyplot as plt
from itertools import count
from tqdm import tqdm
from collections import defaultdict
import numpy as np
from termcolor import colored

start_time = time.time()


#my_file = open("sample.txt", "r") 
#my_file = open("sample2.txt", "r") 
#my_file = open("sample3.txt", "r") 
my_file = open("input.txt", "r")
data = my_file.read()
paths = [[j for j in i] for i in data.split("\n")]
my_file.close()

def part_1():
    print("starting position")
    for row in paths:
        print(row)
    path = copy.deepcopy(paths)
    prev_path = copy.deepcopy(paths)
    for num_steps in range(100):
        path = copy.deepcopy(prev_path)
        for idx,i in enumerate(path):
            for idy,y in enumerate(i):
                if idx == 0:
                    pass
                else:
                    if y == "O":
                        if path[idx-1][idy] == ".":
                            path[idx-1][idy] = "O"
                            path[idx][idy] = "."
        if path == prev_path:
            print("Final position after",num_steps)
            for row in path:
                print("".join(row))
            break
        else:
            prev_path = path
            print("position after",num_steps)
            for row in path:
                print(row)
    ans = 0
    for idx,i in enumerate(path):
        for idy,y in enumerate(i):
            if y == "O":
                ans = ans + len(path)-idx
    print("Part 1:",ans)
        

def part_2():
    print("starting position")
    for row in paths:
        print(row)
    path = copy.deepcopy(paths)
    prev_path = copy.deepcopy(paths)
    cycle_path = copy.deepcopy(paths)
    cycle_prev_path = copy.deepcopy(paths)
    cycle_list = []
    cycles = ["north","west",'south',"east"]
    #                         1000000000
    for total_cycles in range(1000000):
        for num_steps in range(4):
            for internal_step in range(1000000):
                path = copy.deepcopy(prev_path)
                for idx,i in enumerate(path):
                    for idy,y in enumerate(i):
                        if y == "O":
                            if num_steps % 4 == 0:
                                if idx != 0 and path[idx-1][idy] == ".":
                                    path[idx-1][idy] = "O"
                                    path[idx][idy] = "."
                            if num_steps % 4 == 1:
                                if idy != 0 and path[idx][idy-1] == ".":
                                    path[idx][idy-1] = "O"
                                    path[idx][idy] = "."
                            if num_steps % 4 == 2:
                                if idx+1 != len(path) and path[idx+1][idy] == ".":
                                    path[idx+1][idy] = "O"
                                    path[idx][idy] = "."
                            if num_steps % 4 == 3:
                                if idy+1 != len(path[0]) and path[idx][idy+1] == ".":
                                    path[idx][idy+1] = "O"
                                    path[idx][idy] = "."
                if path == prev_path:
                    #print("Final position after",cycles[num_steps % 4])
                    #for row in path:
                    #    print("".join(row))
                    break
                else:
                    prev_path = path
                    #print("position after",internal_step)
                    #for row in path:
                    #    print(row)
        cycle_path = copy.deepcopy(path)
        x = []
        for i in cycle_list:
            if i not in x:
                x.append(i)
        res = []
        for i in cycle_list:
            res.append(x.index(i))
        print("Unique IDs:",res)
        print()
        counter_test = Counter(res)
        if len(counter_test) > 1 and counter_test.most_common(1)[0][1] > 3:
            print(counter_test.most_common(1))
            print(counter_test)
            repeating_list = [x for x in counter_test if counter_test[x] > 2]
            print(repeating_list)
            volume = (1000000000 - 1 - min(repeating_list)) % len(repeating_list)
            print("winning path:")
            print(volume)
            print(repeating_list[volume])
            ans = 0
            for idx,i in enumerate(cycle_list[repeating_list[volume]]):
                for idy,y in enumerate(i):
                    if y == "O":
                        ans = ans + len(path)-idx
            print("Part 2:",ans)
            exit()
        cycle_list.append(cycle_path)
        if cycle_prev_path == cycle_path:
            print("Final position after cycle count:",total_cycles)
            for row in path:
                print("".join(row))
            break
        else:
            cycle_prev_path = path


#part_1()
part_2()
print('[Finished in {:.2f}ms]'.format(1000*(time.time() - start_time)))
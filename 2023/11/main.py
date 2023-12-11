import time
from collections import Counter
import re
import copy
from math import dist
import sys
import cv2
import matplotlib.pyplot as plt
import numpy as np

from termcolor import colored

sys.setrecursionlimit(100000)

start_time = time.time()


#my_file = open("sample.txt", "r") 
#my_file = open("sample2.txt", "r") 
#my_file = open("sample3.txt", "r") 
my_file = open("input.txt", "r")
data = my_file.read()
paths = [[j=="#" for j in i] for i in data.split("\n")]
#print(paths)
my_file.close()
shape_arr = []

def part_1(paths):
    #print("Part 1:")
    found=False
    for idx,i in enumerate(paths):
        if found:
            found=False
        elif all([j==False for j in i]):
            #print("Row blank:",idx)
            paths.insert(idx,i)
            found = True
    found=False
    paths_t = list(zip(*paths))
    for idx,i in enumerate(paths_t):
        if found:
            found=False
        elif all([j==False for j in i]):
            #print("Row blank:",idx)
            paths_t.insert(idx,i)
            found = True
    paths = list(zip(*paths_t))
    galaxies = []
    for idx,i in enumerate(paths):
        for idy,j in enumerate(i):
            if j==True:
                galaxies.append([idx,idy])
    #print(galaxies)
    ans = []
    for galaxy in galaxies:
        for galaxy2 in galaxies:
            ans.append(dist([galaxy[0]],[galaxy2[0]])+dist([galaxy[1]],[galaxy2[1]]))
    print("Part 1:",sum(ans)/2)


def part_2(paths,expansion=1):
    #print("Part 1:")
    found=0
    distance_chart = [[1 for i in k] for k in paths]
    #for test in distance_chart:
    #    print(test)
    it = enumerate(paths)
    print("adding X Galaxies")
    for idx,i in it:
        if all([j==False for j in i]):
            distance_chart[idx] = [expansion for j in i]
    found=0
    paths_t = list(zip(*paths))
    distance_chart2 = list(zip(*distance_chart))
    print("adding Y Galaxies")
    it = enumerate(paths_t)
    for idx,i in it:
        if all([j==False for j in i]):
            distance_chart2[idx] = [expansion for j in i]
    paths = list(zip(*paths_t))
    distance_chart = list(zip(*distance_chart2))
    #for test in distance_chart:
    #    print(test)
    #for i in paths:
    #    print(i)
    galaxies = []
    print("Finding Galaxies")
    for idx,i in enumerate(paths):
        for idy,j in enumerate(i):
            if j==True:
                galaxies.append([idx,idy])
    #print(galaxies)
    ans = []
    print("Calculating Galaxies")
    for galaxy in galaxies:
        for galaxy2 in galaxies:
            temp_ans = 0
            for i in range(min([galaxy[0],galaxy2[0]]),max([galaxy[0],galaxy2[0]])):
                temp_ans = temp_ans + distance_chart[i][min([galaxy[1],galaxy2[1]])]
            for j in range(min([galaxy[1],galaxy2[1]]),max([galaxy[1],galaxy2[1]])):
                temp_ans = temp_ans + distance_chart[max([galaxy[0],galaxy2[0]])][j]
            ans.append(temp_ans)
    #print(ans)
    print("Part 2:",sum(ans)/2)

paths_pt1 = copy.deepcopy(paths)
paths_pt2 = copy.deepcopy(paths)

part_1(paths_pt1)
part_2(paths_pt2,(1000000))
print('[Finished in {:.2f}ms]'.format(1000*(time.time() - start_time)))
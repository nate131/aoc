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
paths = [[[i] for i in j] for j  in data.split("\n")]
my_file.close()

CACHE = []

    
def part_1():
    global CACHE
    actions = [[0,0,"E"]]
    while len(actions) > 0:
        step = actions.pop()
        if step == [None]:
            continue
        actions.extend(take_path(step[0],step[1],step[2],paths))
    energy_list = [i[:-1] for i in CACHE]
    print(energy_list)
    energy_list.sort()
    ans = list(energy_list for energy_list,_ in itertools.groupby(energy_list))
    print(ans)
    print(len(ans))

def part_2():
    global CACHE
    starting_actions = []
    answer = []
    for i in range(len(paths)):
        starting_actions.append([0,i,"S"])
    for i in range(len(paths)):
        starting_actions.append([i,0,"E"])
    for i in range(len(paths)):
        starting_actions.append([len(paths)-1,i,"N"])
    for i in range(len(paths)):
        starting_actions.append([i,len(paths[0])-1,"W"])
    #starting_actions.append([0,3,"S"])
    #print(starting_actions)
    #for starter in tqdm(starting_actions):
    for starter in tqdm(starting_actions):
        #print(starter)
        CACHE = []
        actions = []
        actions.append(starter)
        while len(actions) > 0:
            step = actions.pop()
            #print(step)
            if step != [None]:
                actions.extend(take_path(step[0],step[1],step[2],paths))
        energy_list = [i[:-1] for i in CACHE]
        #print(energy_list)
        energy_list.sort()
        ans = list(energy_list for energy_list,_ in itertools.groupby(energy_list))
        #print(ans)
        answer.append(len(ans))
        #print(starter,"score",len(ans),answer)
    print("Part 2:",max(answer))
    
def take_path(x,y,direction,map):
    global CACHE
    if x < 0 or y < 0 or x >= len(map) or y >= len(map[0]):
        #print(x,y,"Out of Bounds")
        return [[None]]
    if [x,y,direction] in CACHE:
        #print("Already performed",x,y,direction)
        return [[None]]
    else:
        CACHE.append([x,y,direction])
    #print(map[x][y],direction)
    if map[x][y] == ["."]:
        #print("Found . at ",x,y)
        if direction == "N":
            return [[x-1,y,"N"]]
        if direction == "E":
            return [[x,y+1,"E"]]
        if direction == "S":
            return [[x+1,y,"S"]]
        if direction == "W":
            return [[x,y-1,"W"]]
    if map[x][y] == ["/"]:
        if direction == "N":
            return [[x,y+1,"E"]]
        if direction == "E":
            return [[x-1,y,"N"]]
        if direction == "S":
            return [[x,y-1,"W"]]
        if direction == "W":
            return [[x+1,y,"S"]]
    if map[x][y] == ["\\"]:
        if direction == "N":
            return [[x,y-1,"W"]]
        if direction == "E":
            return [[x+1,y,"S"]]
        if direction == "S":
            return [[x,y+1,"E"]]
        if direction == "W":
            return [[x-1,y,"N"]]
    if map[x][y] == ["-"]:
        if direction == "N":
            return [[x,y-1,"W"],[x,y+1,"E"]]
        if direction == "E":
            return [[x,y+1,"E"]]
        if direction == "S":
            return [[x,y-1,"W"],[x,y+1,"E"]]
        if direction == "W":
            return [[x,y-1,"W"]]
    if map[x][y] == ["|"]:
        if direction == "N":
            return [[x-1,y,"N"]]
        if direction == "E":
            return [[x+1,y,"S"],[x-1,y,"N"]]
        if direction == "S":
            return [[x+1,y,"S"]]
        if direction == "W":
            return [[x+1,y,"S"],[x-1,y,"N"]]
    print("Error!")
        

part_1()
part_2()
print('[Finished in {:.2f}ms]'.format(1000*(time.time() - start_time)))
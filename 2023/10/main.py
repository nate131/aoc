import time
from collections import Counter
import re
import copy
from math import lcm
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
paths = [[j for j in i] for i in data.split("\n")]
#print(paths)
my_file.close()
shape_arr = []

def part_1():
    #print("Part 1:")
    for idx,row in enumerate(paths):
        for idy,col in enumerate(paths[idx]):
            if col == "S":
                current_pos = [idx,idy]
                numaway = 0
    final_path = allowed_next(*current_pos,paths,numaway,*current_pos)
    #print(final_path)
    #print(numaway)
    #for lines in final_path[1]:
    #    print("".join(lines))
    pts=[np.array(shape_arr)]
    a3 = np.array( [shape_arr], dtype=np.int32 )
    im = np.zeros([len(paths),len(paths[0])],dtype=np.uint8)
    cv2.fillPoly( im, a3, 1 )
    print("Part1: ",final_path[0]/2)
    print("Part2:",np.count_nonzero(im)-final_path[0])
    #print(current_pos)

def allowed_next( idx,idy,paths,numaway,start_idx,start_idy,last_action="S",last_dir="None"):
    global shape_arr
    numaway = numaway + 1
    up = idx-1 >= 0 and idx-1 <= len(paths) and (paths[idx][idy] in ["|",'L','J'] or last_action == "S") and last_dir != "down"
    left = idy-1 >=0 and idy-1 <= len(paths[0]) and (paths[idx][idy] in ['7','-','J'] or last_action == "S") and last_dir != "right"
    right = idy+1 >=0 and idy+1 <= len(paths[0]) and (paths[idx][idy] in ['L','-','F'] or last_action == "S") and last_dir != "left"
    down = idx+1 >= 0 and idx+1 <= len(paths) and (paths[idx][idy] in ['|','7','F'] or last_action == "S") and last_dir != "up"
    #print(idx,len(paths),last_action,last_dir)
    #print(up,left,right,down)
    shape_arr.append([idx,idy])
    current_pipe = paths[idx][idy]
    paths[idx][idy] = colored(paths[idx][idy], 'red')
    if numaway > 1 and idx==start_idx and idy==start_idy:
        #print(numaway)
        return numaway
    if up:
        #print("UP")
        if paths[idx-1][idy] == "|":
            return allowed_next(idx-1,idy,paths,numaway,start_idx,start_idy,current_pipe,"up")
        if paths[idx-1][idy] == "7":
            return allowed_next(idx-1,idy,paths,numaway,start_idx,start_idy,current_pipe,"up")
        if paths[idx-1][idy] == "F":
            return allowed_next(idx-1,idy,paths,numaway,start_idx,start_idy,current_pipe,"up")
    if left:
        #print("LEFT")
        if paths[idx][idy-1] == "-":
            return allowed_next(idx,idy-1,paths,numaway,start_idx,start_idy,current_pipe,"left")
        if paths[idx][idy-1] == "L":
            return allowed_next(idx,idy-1,paths,numaway,start_idx,start_idy,current_pipe,"left")
        if paths[idx][idy-1] == "F":
            return allowed_next(idx,idy-1,paths,numaway,start_idx,start_idy,current_pipe,"left")
    if right:
        #print("RIGHT")
        if paths[idx][idy+1] == "-":
            return allowed_next(idx,idy+1,paths,numaway,start_idx,start_idy,current_pipe,"right")
        if paths[idx][idy+1] == "J":
            return allowed_next(idx,idy+1,paths,numaway,start_idx,start_idy,current_pipe,"right")
        if paths[idx][idy+1] == "7":
            return allowed_next(idx,idy+1,paths,numaway,start_idx,start_idy,current_pipe,"right")
    if down:
        #print("DOWN")
        if paths[idx+1][idy] == "|":
            return allowed_next(idx+1,idy,paths,numaway,start_idx,start_idy,current_pipe,"down")
        if paths[idx+1][idy] == "J":
            return allowed_next(idx+1,idy,paths,numaway,start_idx,start_idy,current_pipe,"down")
        if paths[idx+1][idy] == "L":
            return allowed_next(idx+1,idy,paths,numaway,start_idx,start_idy,current_pipe,"down")
    #print(paths)
    return [numaway,paths]
    



part_1()
print('[Finished in {:.2f}ms]'.format(1000*(time.time() - start_time)))
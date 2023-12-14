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

import numpy as np
from termcolor import colored

start_time = time.time()


#my_file = open("sample.txt", "r") 
#my_file = open("sample2.txt", "r") 
#my_file = open("sample3.txt", "r") 
my_file = open("input.txt", "r")
data = my_file.read()
paths = [[[k for k in j] for j in i.split("\n")] for i in data.split("\n\n")]
my_file.close()

def part_1():
    ans = 0
    for idx, i in enumerate(paths):
        #print("mirrors:",idx)
        #for k in i:
        #    print(k)
        ans = ans + find_match(i,100)
        transposed = list(zip(*i))
        ans = ans + find_match(transposed,1)
    print("Part 1:",ans)

def find_match(i,multiplier):
    prev_test = []
    ans = 0
    for idy, k in enumerate(i):
        if prev_test == k:
            #print("match on row",idy,idy-1)
            match_row = idy
            row_limit = min([len(i)-1-idy,idy-1])
            #print(row_limit)
            success = True
            for j in range(0,row_limit):
                if i[idy-2-j] == i[idy+1+j]:
                    #print("Match on:",idy-2-j,idy+1+j)
                    pass
                else:
                    #print("No Match on:",idy-2-j,idy+1+j)
                    success = False
                    break
            if success == False:
                prev_test = k
            else:
                #print("SUCCESS on",idy,"ans=+",(idy*multiplier))
                ans = ans + (idy*multiplier)
        else:
            prev_test = k
    return ans

def part_2():
    ans = 0
    for idx, i in enumerate(paths):
        #print("mirrors:",idx)
        #for k in i:
        #    print(k)
        #print("horizontal Testing")
        hori = find_match2(i,100)
        if hori == 0:
            transposed = list(zip(*i))
            #print("vert Testing")
            vert = find_match2(transposed,1)  
            if vert == 0:
                print("Something broken")
            else:
                ans = ans + vert
        else:
            ans = ans + hori
    print("Part 2:",ans)

def find_match2(i,multiplier):
    prev_test = []
    ans = 0
    for idy, k in enumerate(i):
        smudges_used = 0
        if prev_test == k:
            #print("match on row",idy,idy-1)
            match_row = idy
            row_limit = min([len(i)-1-idy,idy-1])
            #print(row_limit)
            success = True
            for j in range(0,row_limit):
                if i[idy-2-j] == i[idy+1+j]:
                    #print("Match on:",idy-2-j,idy+1+j)
                    pass
                elif smudges_used == 0 and sum(1 for k_test, j_test in zip(i[idy+1+j], i[idy-2-j]) if k_test != j_test) == 1:
                    #print("Match on:",idy-2-j,idy+1+j)
                    smudges_used = smudges_used + 1
                else:
                    #print("No Match on:",idy-2-j,idy+1+j)
                    success = False
                    break
            if success == False:
                prev_test = k
            elif success == True and smudges_used == 1:
                #print("SUCCESS on",idy,"ans=+",(idy*multiplier))
                ans = ans + (idy*multiplier)
                return ans
        elif sum(1 for k_test, j_test in zip(k, prev_test) if k_test != j_test) == 1:
            smudges_used = 1
            #print("match on row with smudge",idy,idy-1)
            match_row = idy
            row_limit = min([len(i)-1-idy,idy-1])
            #print(row_limit)
            success = True
            for j in range(0,row_limit):
                if i[idy-2-j] == i[idy+1+j]:
                    #print("Match on:",idy-2-j,idy+1+j)
                    pass
                else:
                    #print("No Match on:",idy-2-j,idy+1+j)
                    success = False
                    break
            if success == False:
                prev_test = k
            elif smudges_used == 1:
                #print("SUCCESS on",idy,"ans=+",(idy*multiplier))
                ans = ans + (idy*multiplier)
                return ans
        else:
            prev_test = k
    #print("Something is broken")
    return 0

part_1()
part_2()
print('[Finished in {:.2f}ms]'.format(1000*(time.time() - start_time)))
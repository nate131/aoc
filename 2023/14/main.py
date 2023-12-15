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
paths = data.split(",")
my_file.close()

def part_1():
    #print(paths)
    ans = []
    for i in paths:
        current_value = 0
        for j in i:
            #print(j)
            ascii_code = ord(j)
            current_value = current_value + ascii_code
            current_value = current_value * 17
            current_value = current_value % 256
        #print(i,current_value)
        ans.append(current_value)
    print("Part1:",sum(ans))
        

def part_2():
    ans = 0
    boxes = [[] for _ in range(256)]
    for idx,i in enumerate(paths):
        #print()
        #print(idx, "STEP",i)
        if i.count("-") > 0:
            #print("- found in path",idx)
            box_id = hash_it(i[:i.index("-")])
            #print(box_id,"box id found from hash")
            for lenid,lense in enumerate(boxes[box_id]):
                if i[:i.index("-")] == lense[:i.index("-")]:
                    boxes[box_id].pop(lenid)
                    #print("removed",i[:i.index("-")],"from",box_id)
        if i.count("=") > 0:
            box_id = hash_it(i[:i.index("=")])
            #print(box_id,"box id found from hash")
            power = i[i.index("="):]
            #print(power,"power found")
            found=False
            for lenid,lense in enumerate(boxes[box_id]):
                #print("checking if",i.replace("="," ").split(" ")[0],"==",lense.split(" ")[0])
                if i.replace("="," ").split(" ")[0] == lense.split(" ")[0]:
                    #print("MATCH!",box_id,lenid,"to be replaced with",i.replace("="," "))
                    found=True
                    boxes[box_id][lenid] = i.replace("="," ")
            if not found:
                boxes[box_id].append(i.replace("="," "))
        #for boxid, box in enumerate(boxes):
        #    if box != []:
        #        print(boxid,box)
    for boxid,box in enumerate(boxes):
        for itemid,item in enumerate(box):
            ans = ans + ((boxid+1) * (itemid+1) * int(item.split(" ")[1]))
    print("Part 2:",ans)

def hash_it(input):
    current_value = 0
    for j in input:
        #print(j)
        ascii_code = ord(j)
        current_value = current_value + ascii_code
        current_value = current_value * 17
        current_value = current_value % 256
    return current_value

part_1()
part_2()
print('[Finished in {:.2f}ms]'.format(1000*(time.time() - start_time)))
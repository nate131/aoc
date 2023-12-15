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
paths = [[i.split(" ")[0],i.split(" ")[1].split(",")] for i in data.split("\n")]
#print(paths)
my_file.close()

def part_1():
    options = ["#", "."]
    answer = 0
    for idx,i in tqdm(enumerate(paths)):
        original_test = copy.deepcopy(i)
        num_hash = i[0].count("?")
        test_list = list(itertools.product(options, repeat=num_hash))
        #print(test_list)
        for j in test_list:
            test = copy.deepcopy(original_test)
            counter = iter(j)
            #print(counter)
            #print(test,j)
            new_string = re.sub(r'\?', lambda x: str(next(counter)), "".join(test[0]) )
            if match_check2(new_string,i[1]):
                answer = answer + 1
    print("Part 1:",answer)

def match_check(input,seq):

    groups = input.split(".")
    counts = []
    for checks in groups:
        counts.append(checks.count("#"))
    #print(input)
    if [int(i) for i in seq] == [item for item in counts if item != 0]:
        return True
    else:
        return False

def match_check2(input,seq):
    str = '^\.*'
    for i in seq:
        str = str+"#{"+i+"}\.+"
    pattern = re.compile(str[:-3]+"\.*$")
    #print(str[:-3],input,pattern.match(input))
    #if pattern.match(input):
    #    print(pattern.match(input))
    return pattern.match(input)

#961120186346
#959690023215


def part_2(multiplier=1):
    options = ["#", "."]
    
    answer_list = []
    for idx,i in enumerate(paths):
        answer = 0
        answer_list.append([])
        idx_ans = 0
        original_test = copy.deepcopy(i[0])
        if re.search(r'^#+\.', original_test):
            original_test = original_test+"."
        else:
            original_test = original_test+"?"
        test_string = (original_test*multiplier)
        test_seq = i[1]*multiplier

        original_test = copy.deepcopy(i)
        num_hash = test_string.count("?")
        #print("Creating Product")
        test_list = itertools.product(options, repeat=num_hash)
        #print("Finished Creating Product")
        #print(test_list)
        for j in test_list:
                counter = iter(j)
                #print(counter)
                #print(test,j)
                new_string = re.sub(r'\?', lambda x: str(next(counter)), "".join(test_string) )
                #print(new_string)
                if match_check2(new_string,test_seq):
                    answer = answer + 1
        answer_list[idx].append(answer)
    for idx,i in enumerate(paths):
        answer = 0
        idx_ans = 0
        original_test = copy.deepcopy(i[0])
        if re.search(r'\.#+$', original_test):
            original_test = "."+original_test
        else:
            original_test = "?"+original_test
        test_string = (original_test*multiplier)
        test_seq = i[1]*multiplier

        num_hash = test_string.count("?")
        #print("Creating Product")
        test_list = itertools.product(options, repeat=num_hash)
        #print("Finished Creating Product")
        #print(test_list)
        for j in test_list:
                counter = iter(j)
                #print(counter)
                #print(test,j)
                new_string = re.sub(r'\?', lambda x: str(next(counter)), "".join(test_string) )
                #print(new_string)
                if match_check2(new_string,test_seq):
                    answer = answer + 1
        answer_list[idx].append(answer)
    
    for item in answer_list:
        print(item,max( (item[0]**4)*(item[1]**1) ,(item[1]**4)*(item[0]**1)))
    print(sum([max( (item[0]**4)*(item[1]**1) ,(item[1]**4)*(item[0]**1)) for item in answer_list]))


#part_1()
part_2(2)
print('[Finished in {:.2f}ms]'.format(1000*(time.time() - start_time)))
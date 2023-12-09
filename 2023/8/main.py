import time
from collections import Counter
import re
import copy
from math import lcm
start_time = time.time()


def part_1():
    print("Part 1:")
    pathways = []
    for path in paths:
        pathways.append(re.findall(r'([A-Z]{3})',path))
    #print(pathways)
    maps = {i[0]:[i[1],i[2]] for i in pathways}
    #print(maps)
    current_location = 'AAA'
    ans = 0
    for _ in range(100):
        if current_location != "ZZZ":
            for step in steps:
                ans = ans + 1
                if step == "R":
                    current_location = maps[current_location][1]
                else:
                    current_location = maps[current_location][0]
                #print(current_location)
                if current_location == "ZZZ":
                    break
    print(ans)

def part_2():
    print("Part 2:")
    pathways = []
    #print(paths)
    for path in paths:
        pathways.append(re.findall(r'([0-9,A-Z]{3})',path))
    #print(pathways)
    maps = {i[0]:[i[1],i[2]] for i in pathways}
    #print(maps)
    ends_a = []
    for locs in maps.keys():
        if locs[2] == 'A':
            ends_a.append([locs,0,0])
    #print(ends_a)
    current_location = 'AAA'
    ans = 0
    for _ in range(10000000):
        for step in steps:
            ans = ans + 1
            for idx,ghost in enumerate(ends_a):
                ends_a[idx][0] = perform_step(ghost[0],step,maps)
                if ends_a[idx][0][2] == "Z":
                    ends_a[idx][2] = ends_a[idx][1] + 1
                    ends_a[idx][1] = 0
                else:
                    ends_a[idx][1] = ends_a[idx][1] + 1
            print(ends_a)
            if all(i[2] > 0 for i in ends_a):
                lcm_inputs = [i[2] for i in ends_a]
                print(*lcm_inputs)
                print(lcm(*lcm_inputs))
                return "done"

def perform_step(current_location,dir,maps):
    if dir == "R":
        return maps[current_location][1]
    else:
        return maps[current_location][0]



#my_file = open("sample.txt", "r") 
#my_file = open("sample2.txt", "r") 
#my_file = open("sample3.txt", "r") 
my_file = open("input.txt", "r")
data = my_file.read()
steps, paths = data.split("\n\n")
paths = paths.split("\n")
my_file.close()


part_1()


#my_file = open("sample.txt", "r") 
#my_file = open("sample2.txt", "r") 
#my_file = open("sample3.txt", "r") 
my_file = open("input.txt", "r")
data = my_file.read()
steps, paths = data.split("\n\n")
paths = paths.split("\n")
my_file.close()

part_2()
print("--- %s seconds ---" % (time.time() - start_time))

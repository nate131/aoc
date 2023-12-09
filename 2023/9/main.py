import time
from collections import Counter
import re
import copy
from math import lcm
start_time = time.time()


#my_file = open("sample.txt", "r") 
#my_file = open("sample2.txt", "r") 
#my_file = open("sample3.txt", "r") 
my_file = open("input.txt", "r")
data = my_file.read()
paths = data.split("\n")
my_file.close()


def part_1():
    print("Part 1:")
    print(paths)
    rounds = [[[int(a) for a in path.split(" ")]] for path in paths]
    for idx,round in enumerate(rounds):
        #print(round)
        level = 0

        while not all([a==0 for a in round[level]]):
            #print(all([a==0 for a in round[level]]))
            #print([a==0 for a in round[level]])
            #print("sending to calcy:",round[level])
            rounds[idx].append(next_level(round[level]))
            level = level+1
            if round[level] == []:
                exit()
    ans = []
    for idx,round in enumerate(rounds):
        round_next = sum([a[-1] for a in round])
        ans.append(round_next)
    print("Part 1: ",sum(ans))

def next_level(round,dir=True):
    next_lvl = []
    #print("Round:",round)
    for idy,item in enumerate(round):
        if idy < len(round)-1:
            if dir:
                next_lvl.append(int(round[idy+1])-int(round[idy]))
            else:
                next_lvl.append(int(round[idy])-int(round[idy+1]))
    #print(next_lvl)
    #print("Calcy Returning:",next_lvl)
    return next_lvl


def part_2():
    print("Part 2:")
    print(paths)
    rounds = [[[int(a) for a in path.split(" ")]] for path in paths]
    for idx,round in enumerate(rounds):
        #print(round)
        level = 0

        while not all([a==0 for a in round[level]]):
            #print(all([a==0 for a in round[level]]))
            #print([a==0 for a in round[level]])
            #print("sending to calcy:",round[level])
            rounds[idx].append(next_level(round[level],False))
            level = level+1
            if round[level] == []:
                exit()
    ans = []
    for idx,round in enumerate(rounds):
        round_next = sum([a[0] for a in round])
        ans.append(round_next)
    print(ans)
    print("Part 2: ",sum(ans))


part_1()
part_2()
print("--- %s seconds ---" % (time.time() - start_time))

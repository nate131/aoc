import time
import logging
import threading
import time
import copy
from tqdm import tqdm
from multiprocessing import Pool
start_time = time.time()

#my_file = open("sample.txt", "r") 
#my_file = open("sample2.txt", "r") 
my_file = open("input.txt", "r")
data = my_file.read()
input_val = data.split("\n\n")
my_file.close()


def part_1():
    #print("Part 1:")
    seeds = input_val[0].split(" ")[1:]
    ans = []
    #print(seeds)
    map_sets = [ {'level': x, 'rules':[]} for x in range(0,len(input_val[1:])) ]
    for idx,maps in enumerate(input_val[1:]):
        #print(maps.split("\n")[1:])
        for item in maps.split("\n")[1:]:
            start = int(item.split(" ")[1])
            end = int(item.split(" ")[0])
            range_num = int(item.split(" ")[2])
            map_sets[idx]['rules'].append([start,end,range_num])
    #print(map_sets)
    for seed in seeds:
        current_value = copy.copy(int(seed))
        pathway = [current_value]
        for level in range(0,len(input_val[1:])):
            complete = False
            for rule in map_sets[level]['rules']:
                if complete == False:
                    if current_value >= rule[0] and current_value <= (rule[2]+rule[0]-1):
                        current_value = current_value - rule[0] + rule[1]
                        complete = True
            pathway.append(current_value)
        #print(seed, current_value)
        #print(pathway)
        ans.append(current_value)
    ans.sort()
    print("Part 1:",ans[0])


def part_2(start_num=0,end_num=1,jump=1,id=0):
    #print("Part 2 Thread Start:",start,end,jump,id)
    seeds = input_val[0].split(" ")[1:]
    ans = []
    #print(seeds)
    map_sets = [ {'level': x, 'rules':[]} for x in range(0,len(input_val[1:])) ]
    for idx,maps in enumerate(input_val[1:]):
        #print(maps.split("\n")[1:])
        for item in maps.split("\n")[1:]:
            start = int(item.split(" ")[1])
            end = int(item.split(" ")[0])
            range_num = int(item.split(" ")[2])
            map_sets[idx]['rules'].append([start,end,range_num])
    #print(map_sets)
    map_sets.reverse()
    seed_pairs = [seeds[i:i+2] for i in range(0,len(seeds), 2)]
    #print(seed_pairs)
    min_seed = 999999999999999999999
    #for seed in trange(start_num,end_num,jump,position=id,desc='Thread #{id}'.format(id=id),leave=False):
    for seed in range(start_num,end_num,jump):
        current_value = copy.copy(int(seed))
        pathway = [current_value]
        for level in range(0,len(input_val[1:])):
            complete = False
            for rule in map_sets[level]['rules']:
                if complete == False:
                    if current_value >= rule[1] and current_value <= (rule[2]+rule[1]-1):
                        current_value = current_value - rule[1] + rule[0]
                        complete = True
            pathway.append(current_value)
        #print(seed, current_value)
        #print(pathway)
        #print("Tested",seed, "got",current_value)
        for test in seed_pairs:
            if current_value >= int(test[0]) and current_value <= int(int(test[0])+int(test[1])):
                if seed < min_seed:
                    min_seed = seed
    return min_seed
                #print(test)
    #print("Thread",id,"no result")

part_1()

#threads
min = 99999999999999
max = 0
map_sets = [ {'level': x, 'rules':[]} for x in range(0,len(input_val[1:])) ]
for idx,maps in enumerate(input_val[1:]):
    #print(maps.split("\n")[1:])
    for item in maps.split("\n")[1:]:
        start = int(item.split(" ")[1])
        end = int(item.split(" ")[0])
        range_num = int(item.split(" ")[2])
        if start < min:
            min=start
        if (start+range_num) > max:
            max=start+range_num
NUM_CORES = 5000


chunk_size = round((max-min) / NUM_CORES)
result = []
MIN_VALUE=9999999999999999
PBAR = tqdm(total=NUM_CORES)
PROCESSES = 14
CURRENT_COMPLETE = 0
POOL = Pool(processes=PROCESSES)
CURRENT_MIN_VALUE_PROCESS=0
def collect_result(val):
    global PBAR
    global MIN_VALUE
    global CURRENT_COMPLETE
    global PROCESSES
    global CURRENT_MIN_VALUE_PROCESS
    PBAR.update(1)
    CURRENT_COMPLETE = CURRENT_COMPLETE + 1
    if val is not None:
        if val < MIN_VALUE:
            MIN_VALUE = val
            CURRENT_MIN_VALUE_PROCESS = CURRENT_COMPLETE
            print("New Min Value:",MIN_VALUE)
    if (CURRENT_COMPLETE > CURRENT_MIN_VALUE_PROCESS + PROCESSES) and MIN_VALUE !=9999999999999999:
        POOL.terminate()
    return result.append(val)
def error_result(val):
    print(f"writing error {val}")
    return result.append(val)
result_f = ''
result_final=[]

for x in range(0,NUM_CORES):
    #print("Starting Thread:",x)
    result_f = POOL.apply_async(func=part_2, args=(min+(chunk_size*x),min+(chunk_size*x)+chunk_size,1,x, ), callback=collect_result,error_callback=error_result)
    result_final.append(result_f)
POOL.close()
POOL.join()

#print(results)
#results_vals = results.values().sort()
print("Part 2:",MIN_VALUE)

print("--- %s seconds ---" % (time.time() - start_time))

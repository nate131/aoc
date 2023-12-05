import time
import copy
start_time = time.time()

#my_file = open("sample.txt", "r") 
#my_file = open("sample2.txt", "r") 
my_file = open("input.txt", "r")
data = my_file.read()
input_val = data.split("\n\n")
my_file.close()


def part_1():
    print("Part 1:")
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
        print(seed, current_value)
        print(pathway)
        ans.append(current_value)
    ans.sort()
    print(ans[0])


def part_2(starter=0,jump=1):
    print("Part 2:")
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
    print(seed_pairs)
    for seed in range(starter,100000000000,jump):
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
        print("Tested",seed, "got",current_value)
        for test in seed_pairs:
            if current_value >= int(test[0]) and current_value <= int(int(test[0])+int(test[1])):
                print(seed, "WINNER!!")
                print(test)
                return [seed,jump]

part_1()
vals = part_2(0,10000)
part_2(vals[0]-vals[1],1)
print("--- %s seconds ---" % (time.time() - start_time))

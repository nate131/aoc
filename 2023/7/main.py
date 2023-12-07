import time
from collections import Counter
import copy
start_time = time.time()

#my_file = open("sample.txt", "r") 
#my_file = open("sample2.txt", "r") 
my_file = open("input.txt", "r")
data = my_file.read()
input_val = data.split("\n")
my_file.close()

value = ['A','K','Q','J','T','9','8','7','6','5','4','3','2']
value_j = ['A','K','Q','T','9','8','7','6','5','4','3','2','J']
value.reverse()
value_j.reverse()

def part_1():
    print("Part 1:")
    score_list = []
    for line in input_val:
        split_line = line.split(" ")
        score = points(split_line[0])
        newhand = str(score)+split_line[0]
        base10 = 0
        for idx,char in enumerate(newhand):
            #print(newhand,value.index(char), 13, (len(newhand)-idx-1),((value.index(char)) * 13 ** (len(newhand)-idx-1)))
            base10 = base10 + ((value.index(char)) * 13 ** (len(newhand)-idx-1))
        #print("Score",newhand,base10)
        
        #print(score)
        #print("Value:",float(str(score)+"."+str(base10)))
        score_list.append([base10,int(split_line[1]),split_line[0],newhand])
    #print(score_list)
    score_list = sorted(score_list, key=lambda x: x[0])
    #score_list.reverse()
    answer = 0
    for idx,hand in enumerate(score_list):
        #print(idx,hand,(hand[1] * (idx+1)))
        answer = answer + (hand[1] * (idx+1))
    
    print(answer)

def points(hand):
    distro = Counter(hand)
    hand_vals = list(distro.values())
    print(hand_vals)
    if 5 in hand_vals:
        return 8
    if 4 in hand_vals:
        return 7
    if 3 in hand_vals and 2 in hand_vals:
        return 6
    if 3 in hand_vals:
        return 5
    if hand_vals.count(2) == 2:
        return 4
    if hand_vals.count(2) == 1:
        return 3
    else:
        return 2

def points_j(hand):
    distro = Counter(hand)
    hand_vals = list(distro.values())
    if 'J' in distro:
        j_count = distro['J']
    else:
        j_count = 0
    print(hand_vals)
    if 5 in hand_vals:
        return 8
    if 4 in hand_vals and j_count >= 1:
        return 8
    if 4 in hand_vals:
        return 7
    if 3 in hand_vals and 2 in hand_vals and j_count >= 2:
        return 8
    if 3 in hand_vals and 2 in hand_vals and j_count >= 3:
        return 8
    if 3 in hand_vals and 2 in hand_vals:
        return 6
    if 3 in hand_vals and j_count == 3:
        return 7
    if 3 in hand_vals and j_count == 2:
        return 6
    if 3 in hand_vals and j_count == 1:
        return 7
    if 3 in hand_vals:
        return 5
    if hand_vals.count(2) == 2 and j_count == 2:
        return 7
    if hand_vals.count(2) == 2 and j_count == 1:
        return 6
    if hand_vals.count(2) == 2:
        return 4
    if hand_vals.count(2) == 1 and j_count == 1:
        return 5
    if hand_vals.count(2) == 1 and j_count == 2:
        return 5
    if hand_vals.count(2) == 1:
        return 3
    if j_count == 1:
        return 3
    else:
        return 2

def part_2():
    print("Part 2:")
    score_list = []
    for line in input_val:
        split_line = line.split(" ")
        score = points_j(split_line[0])
        newhand = str(score)+split_line[0]
        base10 = 0
        for idx,char in enumerate(newhand):
            print(newhand,value_j.index(char), 13, (len(newhand)-idx-1),((value_j.index(char)) * 13 ** (len(newhand)-idx-1)))
            base10 = base10 + ((value_j.index(char)) * 13 ** (len(newhand)-idx-1))
        print("Score",newhand,base10)
        
        #print(score)
        #print("Value:",float(str(score)+"."+str(base10)))
        score_list.append([base10,int(split_line[1]),split_line[0],newhand])
    #print(score_list)
    score_list = sorted(score_list, key=lambda x: x[0])
    #score_list.reverse()
    answer = 0
    for idx,hand in enumerate(score_list):
        print(idx,hand,(hand[1] * (idx+1)))
        answer = answer + (hand[1] * (idx+1))
    
    print(answer)

part_1()
part_2()
print("--- %s seconds ---" % (time.time() - start_time))

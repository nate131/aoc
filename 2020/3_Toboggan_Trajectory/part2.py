import csv
import os
print(os.path.dirname(os.path.realpath(__file__)))
with open(os.path.dirname(os.path.realpath(__file__))+'/input.txt', 'r') as f:
    content = [line.rstrip() for line in f]


def route_test(right,down,pos_x=0,counter=0): 
    for pos_y in range(0,len(content),down):
        if content[pos_y][pos_x] == '#': counter += 1
        pos_x = (pos_x + right) % len(content[0])
    return counter

print(
    route_test(right=1,down=1) *
    route_test(right=3,down=1) *
    route_test(right=5,down=1) *
    route_test(right=7,down=1) *
    route_test(right=1,down=2)
 )
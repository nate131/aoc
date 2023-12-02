import csv
from collections import Counter
import os
import re
print(os.path.dirname(os.path.realpath(__file__)))
with open(os.path.dirname(os.path.realpath(__file__))+'/input.txt', 'r') as f:
    content = f.read().split("\n")
acc = 0
current_line=0
run_lines = []
x=False

while x==False:
    if current_line in run_lines:
        print("ACC as of Inifinite Loop:",acc)
        x=True
        continue
    else:
        run_lines.append(current_line)
    instruction = content[current_line].split(" ")[0]
    value = int(content[current_line].split(" ")[1])
    #print (instruction,value)
    if instruction == "acc": 
        acc += value
    if instruction == "jmp": 
        current_line += value
        continue
    current_line += 1

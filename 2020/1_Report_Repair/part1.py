import csv
import os
print(os.path.dirname(os.path.realpath(__file__)))
with open(os.path.dirname(os.path.realpath(__file__))+'/input.txt', 'r') as f:
    content = [int(line.rstrip()) for line in f]

for i in range(len(content)):
    b = content.index(2020-content[i]) if (2020-content[i]) in content else -1
    if b != -1 : 
        print( i, b, content[i] * content[b] )
        break
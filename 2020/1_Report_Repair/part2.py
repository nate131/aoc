import csv
import os
print(os.path.dirname(os.path.realpath(__file__)))
with open(os.path.dirname(os.path.realpath(__file__))+'/input.txt', 'r') as f:
    content = [int(line.rstrip()) for line in f]

found=False

for i in range(len(content)):
    for j in range(len(content)):
        if (2020-content[i]-content[j]) in content:
            print( content[i] * content[content.index(2020-content[i]-content[j])] * content[j] )
            found=True
            break
    if found==True:
        break
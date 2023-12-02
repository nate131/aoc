import csv
from collections import Counter
import os
import re
from datetime import datetime
startTime = datetime.now()

print(os.path.dirname(os.path.realpath(__file__)))
with open(os.path.dirname(os.path.realpath(__file__))+'/input.txt', 'r') as f:
    content = f.read().split("\n")

map_object = map(int,content)
content = list(map_object)

preamble_len = 25

for i in range(preamble_len,len(content)):
    success = False
    broken_range = False
    for x in content[i-preamble_len:i]:
        for y in content[i-preamble_len:i]:
            if x + y == content[i]: 
                success = True
    if success != True: 
        print("Broken Num:",content[i])
        break
print(datetime.now() - startTime)
import csv
import os
print(os.path.dirname(os.path.realpath(__file__)))
with open(os.path.dirname(os.path.realpath(__file__))+'/input.txt', 'r') as f:
    content = [line.rstrip() for line in f]

counter = 0

for i in range(len(content)):
    pw = content[i].split(":")[1].strip()
    low = int(content[i].split(":")[0].split(" ")[0].split("-")[0])
    high = int(content[i].split(":")[0].split(" ")[0].split("-")[1])
    letter = content[i].split(":")[0].split(" ")[1]
    if bool( pw[low-1] == letter ) != bool( pw[high-1] == letter ):
        counter += 1

print(counter)
import csv
import os
print(os.path.dirname(os.path.realpath(__file__)))
with open(os.path.dirname(os.path.realpath(__file__))+'/input.txt', 'r') as f:
    content = [line.rstrip() for line in f]

counter = 0

for i in range(len(content)):
    parts = content[i].split(":")
    ranges = parts[0].split(" ")[0].split("-")
    letter = parts[0].split(" ")[1]
    if parts[1].count(letter) >= int(ranges[0]) and parts[1].count(letter) <= int(ranges[1]):
        print("Valid PW '"+parts[1]+"' Contains between '"+ranges[0]+"' and '"+ranges[1]+"' '"+letter+"'s")
        counter += 1

print(counter)
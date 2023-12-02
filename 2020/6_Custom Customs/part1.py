import csv
from collections import Counter
import os
print(os.path.dirname(os.path.realpath(__file__)))
with open(os.path.dirname(os.path.realpath(__file__))+'/input.txt', 'r') as f:
    content = f.read().split("\n\n")

    numQ = 0
for group in range(len(content)):
    content[group] = content[group].split("\n")
    letterCounter = Counter()
    for person in content[group]:
        letterCounter += Counter(person)
    for letter in letterCounter:
        numQ += 1
    print(content[group], letterCounter, numQ)
print(numQ)
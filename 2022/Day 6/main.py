from os import path
from time import time
from datetime import timedelta
import profile
import re

# General Setup
start = time()
day = path.basename(path.dirname(path.realpath(__file__)))
input_filename = "input.txt"        # Enable full
#input_filename = "input_test.txt"  # Enable Test
input = path.join(path.dirname(path.realpath(__file__)),input_filename)
with open(input, 'r') as fd:
    data = fd.read()  # list
    #data = [[int(number) for number in split_data.split('\n')] for split_data in fd.read().split('\n\n')] # int-list of lists
ans = ""
print(data)
for i in range(len(data)):
	#print([*data[i:i+4]])
	signal = set([*data[i:i+4]])
	#print(len(signal))
	if len(signal) == 4:
		ans = i+4
		break

print("Part 1:",ans)
ans = ""
print(data)
for i in range(len(data)):
	#print([*data[i:i+4]])
	signal = set([*data[i:i+14]])
	#print(len(signal))
	if len(signal) == 14:
		ans = i+14
		break



print("Part 2:",ans)
print("Execution Time:",str((time()-start)*1000),"ms")

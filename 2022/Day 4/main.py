from os import path
from time import time
from datetime import timedelta
import profile

# General Setup
start = time()
day = path.basename(path.dirname(path.realpath(__file__)))
input_filename = "input.txt"        # Enable full
#input_filename = "input_test.txt"  # Enable Test
input = path.join(path.dirname(path.realpath(__file__)),input_filename)
with open(input, 'r') as fd:
    data = fd.read().split('\n')  # list
    #data = [[int(number) for number in split_data.split('\n')] for split_data in fd.read().split('\n\n')] # int-list of lists



total=0

for assignment in data:
	sections = assignment.split(",")
	sec1 = [int(x) for x in sections[0].split("-")]
	sec2 = [int(x) for x in sections[1].split("-")]
	if sec1[0] <= sec2[0] and sec1[1] >= sec2[1]:
		total = total + 1
		#print("test1",assignment)
	elif sec2[0] <= sec1[0] and sec2[1] >= sec1[1]:
		total = total + 1
		#print("test2",assignment)
print("Part 1:",total)

total=0
for assignment in data:
	sections = assignment.split(",")
	sec1 = [int(x) for x in sections[0].split("-")]
	sec2 = [int(x) for x in sections[1].split("-")]
	if len(set(range(sec1[0],sec1[1]+1)) & set(range(sec2[0],sec2[1]+1))) > 0:
		total = total + 1


print("Part 2:",total)
print("Execution Time:",str((time()-start)*1000),"ms")

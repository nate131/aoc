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

for bag in data:
	#print(bag)
	compar1 = bag[:len(bag)//2]
	compar2 = bag[len(bag)//2:]
	#print(bag[:len(bag)//2],"|",bag[len(bag)//2:])
	match = list(set(compar1) & set(compar2))
	if match[0].isupper():
		total=total + ord(match[0])-38
		#print(match,ord(match[0])-38)
	else:
		total=total + ord(match[0])-96
		#print(match,ord(match[0])-96)

print("Part 1:",total)


total=0
list_of_groups = zip(*(iter(data),) * 3)

for bag in list_of_groups:
	#print(bag)
	match = list(set(bag[0]) & set(bag[1]) & set(bag[2]))
	if match[0].isupper():
		total=total + ord(match[0])-38
		#print(match,ord(match[0])-38)
	else:
		total=total + ord(match[0])-96
		#print(match,ord(match[0])-96)


print("Part 2:",total)
print("Execution Time:",str((time()-start)*1000),"ms")

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
    data = fd.read().split('\n\n')  # list
    #data = [[int(number) for number in split_data.split('\n')] for split_data in fd.read().split('\n\n')] # int-list of lists

print( data[0])
yard = {}
for line in data[0].split('\n')[:-1]:
	#print(line)
	counter = 1
	for i in range(0, len(line), 4):
		#print(line[i:i+4])
		if counter not in yard:
			yard[counter] = []
		if line[i:i+4] == "    " or line[i:i+4] == "   ":
			counter = counter + 1
			continue
		yard[counter].append(re.sub('[\[\] ]', '', line[i:i+4]))
		counter = counter + 1

#print(yard)

moves = []
for line in data[1].split('\n'):
	#print(line)
	splitmoves = line.split(' ')
	moves.append([int(splitmoves[1]),int(splitmoves[3]),int(splitmoves[5])])
	
#print(moves)

for move in moves:
	for i in range(1,move[0]+1):
		#print("moving")
		yard[move[2]] = [yard[move[1]].pop(0)] + yard[move[2]]
	#print("Next Move")
#print(yard)

ans = ""
for stack in yard:
	ans = ans+yard[stack][0]

print("Part 1:",ans)


yard = {}
for line in data[0].split('\n')[:-1]:
	#print(line)
	counter = 1
	for i in range(0, len(line), 4):
		#print(line[i:i+4])
		if counter not in yard:
			yard[counter] = []
		if line[i:i+4] == "    " or line[i:i+4] == "   ":
			counter = counter + 1
			continue
		yard[counter].append(re.sub('[\[\] ]', '', line[i:i+4]))
		counter = counter + 1

#print(yard)

moves = []
for line in data[1].split('\n'):
	#print(line)
	splitmoves = line.split(' ')
	moves.append([int(splitmoves[1]),int(splitmoves[3]),int(splitmoves[5])])
	
#print(moves)

for move in moves:
		yard[move[2]] = yard[move[1]][:move[0]] + yard[move[2]]
		yard[move[1]] = yard[move[1]][move[0]:]
	#print("Next Move")
#print(yard)
ans = ""
for stack in yard:
	ans = ans+yard[stack][0]


print("Part 2:",ans)
print("Execution Time:",str((time()-start)*1000),"ms")

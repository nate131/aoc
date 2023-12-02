from os import path
from time import time
from datetime import timedelta
import profile
import re
import json

# General Setup
start = time()
day = path.basename(path.dirname(path.realpath(__file__)))
input_filename = "input.txt"        # Enable full
#input_filename = "input_test.txt"  # Enable Test
input = path.join(path.dirname(path.realpath(__file__)),input_filename)
with open(input, 'r') as fd:
    data = fd.read().split('\n')  # list
    #data = [[int(number) for number in split_data.split('\n')] for split_data in fd.read().split('\n\n')] # int-list of lists
ans = ""

def is_not_visible(x,y,data):
	#[RIGHT,LEFT,UP,DOWN] bool
	results = [0,0,0,0]
	#right
	for tree in data[x][y+1:]:
		if tree >= data[x][y]:
			#print(x,y,"is not visible as",tree,"is taller RIGHT")
			results[0] = 1
			break
	#left
	for tree in data[x][:y]:
		if tree >= data[x][y]:
			#print(x,y,"is not visible as",tree,"is taller LEFT")
			results[1] = 1
			break
	#up
	for tree in [row[y] for row in data[:x]]:
		if tree >= data[x][y]:
			#print(x,y,"is not visible as",tree,"is taller UP")
			results[2] = 1
			break
	#down
	for tree in [row[y] for row in data[x+1:]]:
		if tree >= data[x][y]:
			#print(x,y,"is not visible as",tree,"is taller DOWN")
			results[3] = 1
			break	
	if results == [1,1,1,1]:
		return True
	return False

visible = (len(data)*4) - 4
for idx, line in enumerate(data[1:-1]):
	for idy, col in enumerate(line[1:-1]):
		if not is_not_visible(idx+1,idy+1,data):
			visible = visible + 1
		else:
			continue
			#print(idx+1,idy+1)

print("Part 1:",visible)




def scenic_score(x,y,data):
	#[RIGHT,LEFT,UP,DOWN] bool
	score = [0,0,0,0]
	#right
	for tree in data[x][y+1:]:
		score[0] = score[0] + 1
		if tree >= data[x][y]:
			break
	#left
	left = [*data[x][:y]]
	print("Left values",left[::-1])
	for tree in left[::-1]:
		score[1] = score[1] + 1
		if tree >= data[x][y]:
			break
	#up
	
	print("Up values",[row[y] for row in data[:x]][::-1])
	for tree in [row[y] for row in data[:x]][::-1]:
		score[2] = score[2] + 1
		if tree >= data[x][y]:
			break
	#down
	for tree in [row[y] for row in data[x+1:]]:
		score[3] = score[3] + 1
		if tree >= data[x][y]:
			break
	print("[",score[2],score[1],score[0],score[3],"]")
	return (score[0] * score[1] * score[2] * score[3])


max_score = 0
for idx, line in enumerate(data[1:-1]):
	for idy, col in enumerate(line[1:-1]):
		score =  scenic_score(idx+1,idy+1,data)
		print(idx+1,idy+1,score)
		print()
		if score > max_score:
			max_score = score

print("Part 2:",max_score)
print("Execution Time:",str((time()-start)*1000),"ms")

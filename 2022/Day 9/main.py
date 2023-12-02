from os import path
from time import time
from datetime import timedelta
import profile
import re
import json
import math

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


def rope_phy(length):
	U = [-1,0]
	D = [1,0]
	L = [0,-1]
	R = [0,1]
	rope = [[0,0]]*length
	seen_positions = [[0,0]]


	for action in data:
		#print("- ",action)
		command = action.split(' ')
		direction = command[0]
		duration = int(command[1])
		for _ in range(duration):
			#print("--moving 1",direction,"need to add",head,"and",locals()[direction])
			#move head
			rope[0] = [sum(i) for i in zip(rope[0], locals()[direction] )]
			#print("Head is now at",head)
			#print("Tail currently",tail)
			#move tail
			#print( [list(i) for i in zip(head, tail )])
			for i in range(len(rope)-1):
				head = rope[i]
				tail = rope[i+1]
				zipped_list = [list(i) for i in zip(head, tail)]
				distance = [math.dist([zipped_list[0][0]],[zipped_list[0][1]])]
				distance.append(math.dist([zipped_list[1][0]],[zipped_list[1][1]]))
				#print("Tail Distance",distance)
				if abs(distance[0]) < 2 and abs(distance[1]) < 2:
					pass
				else:
					#print("TAIL NEEDS TO MOVE")
					if distance[0] == 0 :
						if head[1] > tail[1]:
							#print("Moving R")
							tail = [sum(i) for i in zip(tail, R )]
						else:
							#print("Moving L")
							tail = [sum(i) for i in zip(tail, L )]
					elif distance[1] == 0 :
						if head[0] < tail[0]:
							#print("Moving U")
							tail = [sum(i) for i in zip(tail, U )]
						else:
							#print("Moving D")
							tail = [sum(i) for i in zip(tail, D )]
					else:
						if head[0] > tail[0] and head[1] > tail[1]:
							#print("Moving DR")
							tail = [sum(i) for i in zip(tail, D, R )]
						if head[0] > tail[0] and head[1] < tail[1]:
							#print("Moving DL")
							tail = [sum(i) for i in zip(tail, D, L )]
						if head[0] < tail[0] and head[1] > tail[1]:
							#print("Moving UR")
							tail = [sum(i) for i in zip(tail, U, R )]
						if head[0] < tail[0] and head[1] < tail[1]:
							#print("Moving UL")
							tail = [sum(i) for i in zip(tail, U, L )]
				rope[i] = head
				rope[i+1] = tail
				if i == len(rope)-2 and tail not in seen_positions:
					seen_positions.append(tail)
			#print("Tail now at ",tail,direction)
				#print()
			#print("---------------------")
	return len(seen_positions)

print("Part 1:",rope_phy(2))
print("Part 2:",rope_phy(10))
print("Execution Time:",str((time()-start)*1000),"ms")

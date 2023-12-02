from os import path
from time import time,sleep
from datetime import timedelta
import profile
import re
import json
import math
import random 

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

winners = []
best_winner = 541
max_right = 113
highest_elo = ord('a')
d_record = 414
print_timer = 1000000
current_print = 0
waypoint1_best = 170

def move(pos, map, history):
	global winners
	global best_winner
	global max_right
	global highest_elo
	global current_print
	global print_timer
	global waypoint1_best
	if pos[1] < 113 and len(history) > waypoint1_best:
		#print("failed Way1 Goal")
		return
	if pos[1] == 113 and pos[0] == 22 and len(history) < waypoint1_best:
		print("NEW WAYPOINT1 GOAL",len(history))
		print_map(pos,map,history)
		exit()
	current_print = current_print + 1
	if current_print > print_timer:
		current_print = 0
		print("turn #",len(history))
		print_map(pos,map,history)
	#print(history)
	dirs = [[0,1],[-1,0],[1,0],[0,-1]]
	if len(history) > d_record and highest_elo < ord('d'):
		print("didnt hit d_record")
		return
	if highest_elo < ord(map[pos[0]][pos[1]]):
		highest_elo = ord(map[pos[0]][pos[1]])
		print("New elo Record",chr(highest_elo),"in",len(history),"moves")
		print_map(pos,map,history)
	if max_right < pos[1]:
		max_right = pos[1]
		print("New Right Record",max_right,"in",len(history),"moves")
		print_map(pos,map,history)
	if len(history) > 20 and ((len(history)+1)/ (pos[1]+10) > 1.2) and len(history)< 114:
		return
	if len(history) > best_winner:
		print("lost against best winner")
		sleep(10)
		return
	for dir in dirs:
		if pos[1] < 126 and dir == [0,-1]:
			continue
		new_pos = pos.copy()
		new_history = history.copy()
		new_history.append(pos)
		new_pos = [sum(i) for i in zip(new_pos, dir )]
		if new_pos in history:
			#print("Already been here", history)
			continue
		if new_pos[0] > len(map)-1 or new_pos[1] > len(map[0])-1 or new_pos[0] < 0 or new_pos[1] < 0:
			#print("OOB")
			continue
		#print(new_pos)
		if ord(map[new_pos[0]][new_pos[1]]) > ord(map[pos[0]][pos[1]])+1:
			#print("Too High",map[new_pos[0]][new_pos[1]],map[pos[0]][pos[1]],history)
			continue
		if ord(map[new_pos[0]][new_pos[1]]) < ord(map[pos[0]][pos[1]]) and pos[1] < 125 and ord(map[new_pos[0]][new_pos[1]]) != ord('p') and ord(map[pos[0]][pos[1]]) != ord('r'):
			#print("Too High",map[new_pos[0]][new_pos[1]],map[pos[0]][pos[1]],history)
			continue
		if map[new_pos[0]][new_pos[1]] == "{":
			print("Winner",new_history)
			if best_winner > len(new_history):
				best_winner = len(new_history)
			winners.append(new_history)
			print_map(pos,map,history)
			sleep(10)
			return new_history
		new_history = move(new_pos,map,new_history)
	return new_history

def print_map(pos,map,history):
	print()
	for idx,row in enumerate(map):
		for idy,col in enumerate(row):
			for index in history:
				if index[0] == idx and index[1] == idy:
					col = " "
			print(col,end="")
		print()

"""
abccccaaaaaaaaaaaaaccaaaaaaaacccccccccaaaaaaaaccccccccaaacaaacccccccaaaaaaccccccccccccccccccccccaaaacccccccccccacccccccccccccccccccccccccccccccccccccccccccccccaaaa
abccccaaaaacaaaaaaccccaaaaaaccccccccccaaaaaaacccccccccaaaaaaacccccaaaaaaaaaacccccccccccccccccccaaaaaacccccccccaaaaaaaaccccccccccccccccccccccccccccccccccccccccaaaaa
abcccaaaaaccaaaaaaccccaaaaaaccccccaacccaaaaaacccccccccaaaaaacccaaaaaaaaaaaaaaacaaccacccccccccccaaaaaaccccccccccaaaaaacccccccccccccccccccccccccccccccccccccccccaaaaa
abccccccaaccaaaaaaccaaaaaaaaccccccaaacaaaacaaacccccccaaaaaaaaccaaaaaaaaaaaaaaacaaaaacccccccccccccaaccccccccccccaaaaaaccccccccccccccccccccccccccccacccccccccccaaaaaa
abccccccccccaaccaaccaaaaccaacccccccaaaaaaaccccccccccaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaacccccccaaaaccccccccccccccccaaaaaaaacccccccccccccccccccccccccccaaccccccccccccccaa
abcccccccaaaaacccaaaaaaaacccaaccccaaaaaaccccccccccccaaaaaaaaaaaaaaaacaaaaaaaccaaaaaaccccccaaaaaccccccccccccccaaaaaaaaaaccaccccccccccccccccccccccccaccccccccccccccca
abcccccccaaaaacccaaaaaaaaccaaaaccaaaaaaaaccccccccccccccaaacaaaaaaaaacaaaaaacccccaaaacccccaaaaaaccccccccccccccaaaaaaaaaaaaacccccccccccccccllllllccccdccccccccccccccc
abccccccaaaaaacccccaaaaccccaaaaacaaaaaaaaccccccccccccccaaacccccaaaccccaaaaaacccaaccccccccaaaaaacccccccccccccccccaaaaaaaaaacccccccccccccklllllllllcddddccaccaaaccccc
abccccccaaaaaacccccaaaaaaaaaaaaaaaccaaccccccaacaacccccccaaccccccccccccaaacaacccccccccccccaaaaaacccccccccccccccccaaaaaaaaaacccccccccccckklllppllllcddddddddaaaaccccc
abccccccaaaaaaccccaaacaaaaaaaaaaaaccaaccccccaaaaaccccccccccccccccccccccccccccccccccccccccccaaccccccaaccccccccccccaacaaaaaaaccccccccccckklpppppplllmdddddddddacccccc
abccccccccaaacccccaacccaccaaaaaaccccccccccccaaaaaaccccccccccccccccccccccccccccccccccccccccccccccccaaaaccccccccccccaaaaaaaaaaccccccccckkkkppppppplmmmmmmddddddaacccc
abccccaaacaaacccccccccccccaaaaaaccccccccccccaaaaaacccccccccccccccccaaaccccccccccccccccccccccccccccaaaaccccccccccccaaaaaaaaaaccccccccckkkppppuppppmmmmmmmmddeeeacccc
abccccaaaaaaacccccccccccccaaaaaacccaccccccccaaaaaacccccccccccccccccaaaacccccccccccccccccccccaaacccaaaacccccccccccaaaacaaaccccccccccckkkpppuuuuuppqqmmmmmmmmeeeacccc
abcccccaaaaaaccccccccccccaaaaaaaacaaccccccccccaaaccccccccccccccccccaaaaccccccccccccccccccccaaaaccccc  cccccccccccaaaaaaaacccccccccckkkkpppuuuuupqqqqqqqmmmmeeeccccc
abcccccaaaaaaaacccccccccccaccccaaaaacccccccccccccccccccccccccccccccaaaccccccccccccccaaaccccaaaaccccc    ccccaaccaaaaaaaaccccccccckkkkkrrpuuuxuuuqqqqqqqqmmmmeeccccc
abccccaaaaaaaaaccccccccccccccaaaaaacccccccacaacccccccccccccccccccccccccccccccccccccaaaaaacccaaacccc  cc  aaaaccaaaaaaacccccccccckkkkrrrrruuuxxuvvvvvvqqqqnnneeccccc
abcccaaaaaaaaaaccccccccccccccaaaaaaaacccccaaaaacccccccccccccccaaaaaccccccccccccccccaaaaaacccccccc   cccc aaaaaaaaaaaaacccccccccjjjkrrrrruuuxxxxvvvvvvvqqqnnneeccccc
abcaaaaacaaacccccccccccccccccaaaaaaaacccccaaaaaccaacccccccccccaaaaaccccccccccccccccaaaaaccccccccc cccccc caaaaaccaaaaaacccccccjjjrrrrruuuuuxxxyvyyyvvvqqqnneeeccccc
  caaaaacaaaccaaccccccccccccccccaacccccccaaaaaaaaaaaccccccccccaaaaaaccccccccccccccccaaaaaccc   cc cccccc aaaaacccaaaaaaaacaaacjjjrrrtttuuxxxxxyyyyyvvvqqnnneeeccccc
  aaaaaccaacccaaaccaacccaaccccccaccccccccaaaaaaaaaacccccccccccaaaaaaccccccccccccccccaacaacc  c cc cccccc   caacccaaccccaaaaaacjjjrrrtttxxxxxxxyyyyyvvvrrnnneeeccccc
  aaaaacccccccaaaaaaaccaaaacccccccccccccccaaaaaaaaacccccccccccaaaaaacccccccccccccccccccccc  cc    cccccc     cccccaacccaaaaaacjjjrrrtttxxx{zzzzyyyvvvrrnnneeecccccc
a caaaaacccccccaaaaaaccaaaacccccccccccccccaaaaaaaaacccccccccccccaacccccccccccccccccccccccc cccaacccccccc  aa    acaaaacaaaaaaajjjrrrtttxxxxxyyyyyvvvrrrnnnfffcccccc
a caacccccccaaaaaaaacccaaaaccccccccccccccccaaaaaaaaaaccccccccccccccccccccccccccccccccccccc aaaaaccccccccccaac   aaaaaaaaaaaaaajjjqqqttttxxxxyyyyyyvvrrrnnnfffcccccc
a  cccccccccaaaaaaaaaccccccccccccccccccccaaaaaaaaaaaaacccccccccccccccccaaccccccccccccccccc caaaaaccccccaacaaaaa  aaaacaaaaaaaacjjjqqqqttttxxyywyyyywvrrnnnfffcccccc
ab cccccccccaaaaaaaaaacccccccccccccccccccaaaaaaaaacaaacccccccccccccaaacaaccccccccccccccccc caaaaaccccccaaaaaaaac aaaaccccaaacccjjjjqqqqtttxwywwwyywwwrrnnnfffcccccc
ab   ccccccccccaaaaaaacccccccccccccccccccaaaaaaaaaaaaaaaacccccccccccaaaaaccccccccccccccccc aaaaacccaaccccaaaaccc aacaacccaaacc  jjjiqqqtttwwywwwwwwwwrrroofffcccccc
abcc    cccccccaaaccccccccccccccccccccccaaaaaaaaaaaaaaaaaccccccccccccaaaaaaccccccccccccccc cccaaacaaaccccaaaaacc ccccccccccccc   iiiiqqqttwwwwwswwwwrrrroofffcccccc
abccccc  ccccccaaccccccccccccaaaacccccccaaaaaaaaccaaaaacccccccccccccaaaaaaaccccccccccccccc cccaaaaaaacccaaacaacc   aaaaaccccc    ciiiqqqttwwwwsssssrrrrroofffaccccc
abcccccc     ccccccccccccccccaaaaccccccccacaaacccaaaaaaccccccaaccccaaaaaaccccccccaacaacccc cccaaaaaaccccaaaacacccc aaaaaccccc     iiiqqqtsswsssssssrrrrooofffaccccc
abcccccccccc    cccccccccccccaaaaccccccccccaaaccaaaaaaaccccccaaaaccaacaaaccccccccaaaaacccc ccccaaaaaaaaccaaacacccc aaaaaaccccc     iiqqqssssssspposrrroooofffaccccc
abccccaaacccccc         ccccccaaacccccccccccccccaaacaaaccccaaaaaacccccaaaccccccccaaaaaaccc cccaaaaaaaaaaaaaaaaaccc aaaaaacccc  ac  iiiqqpsssssppppooooooogffaaccccc
abccccaaaaaacccaaaccccc       cccccccccc      ccccccccaccccaaaaacccccccccccccccccaaaaaaccc ccaaaaaaaaaaaaaaaaaaccc aaaaaaccca   c  iiiqqppppppppppoooooogggfaaacccc
abcccaaaaaaacccaaaccccccccccc   ccccc    cccc      cccccccccaaaaac       ccccccccaaaaaaccc ccaaacaaaccccaaaaaacccc   aaccccca      ciiipppppppphgggggggggggaaaacccc
abccaaaaaaaacccaaacaaaccccccccc       cccccaaccccc        ccaacaac cccaa      cccccaaa     ccccccaaacccccaaaaacccccc   cccccc       iiihppppphhhhgggggggggaaccccccc
abccaaaaaaacaaaaaaaaaacccccccccccccccccccccaaaccccccacccc          cccaaccccc          cccccccccaaaaccccaaaaaacccccccc cccccaaa      iihhhhhhhhhhgggggggccaaccccccc
abccccaaaaaaaaaaaaaaacccccccccccccccccccaaaaaaaaccccaaacaaaccccccccccaaaaccaaccccccccaacaacccccaaaaaaacccaaccccccccccc cccccaac      chhhhhhhhhaaaacccccccccccccccc
abccccaaaaaacaaaaaaaccccccccccccccccccccaaaaaaaaccccaaaaaaaccccccccccaaaaaaaacaccccccaaaaaccccccaaaaaccccccccccccccccc cccccccccc ccccchhhhhhacaaaaaccccccccccccccc
abccccaaccccccaaaaaacccccccccccccaaccccccaaaaaacccccaaaaaaccccccaaaaaaaaaaaaaaaccccccaaaaaacccaaaaaaaccccccccccccccccc ccccccc    ccccccccaaaaccaaacccccccccccaaaca
abccccccccccccaaaaaaaccccccccccccaaccccccaaaaaacccaaaaaaaaccccccaaaaaaaaaaaaaacccccccaaaaaacccaaaaaaaaccccccaaaccccccc cccccc  cccccccccccaaaaccccccccccccccccaaaaa
abccaaacccccccaaacaaacccccccccaaaaaaaacccaaaaaacccaaaaaaaaacccccaaaaaaaaaaaaaacccccccaaaaaccccaaaaaaaaccccccaaaacccccc c   cc ccccccccccccaaaccccccccccccccccccaaaa
abcaaaacccccccaaccccccccccccccaaaaaaaacccaaccaacccaaaaaaaaaaccccccccaaaaaaacaacccccccccaaaccccccaaacaaccccccaaaacccccc   c    cccccccccccccccccccccccccccccccaaaaaa

"""


map = []
for line in data:
	map.append([x for x in line])

for idx, row in enumerate(map):
	for idy, col in enumerate(row):
		if col == "S":
			start_pos = [idx,idy]
		if col == "E":
			end_pos = [idx,idy]

print(start_pos)
map[start_pos[0]][start_pos[1]] = "a"
map[end_pos[0]][end_pos[1]] = "{"
move(start_pos, map, [])

winner_lens = []
print(len(winners))
for winner in winners:
	print(winner,len(winner))
	winner_lens.append(len(winner))

print("Part 1:",min(winner_lens))



print("Part 2:",ans)
print("Execution Time:",str((time()-start)*1000),"ms")

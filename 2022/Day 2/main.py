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


points = 0
for battle in data:
	actions = battle.replace("X","1").replace("Y","2").replace("Z","3") \
	.replace("A","1").replace("B","2").replace("C","3").replace(" ","")
	print(actions)
	points = points + int(actions[1])
	if actions[0] == actions[1]:
		points = points + 3
	if (actions[1] == "1" and actions[0] == "3") or \
	(actions[1] == "2" and actions[0] == "1") or \
	(actions[1] == "3" and actions[0] == "2"):
			points = points + 6	
	

print("Part 1:",points)

"""
1,2,3 | rock, paper, scissors
1,2,3 | loose, draw, win
"""

def solver(opp,wld):
	if wld=="2": return opp+opp
	if opp == "1":
		if wld=="1": return opp+"3"
		return opp+"2"
	if opp == "2":
		if wld == "1": return opp+"1"
		return opp+"3"
	if opp == "3":
		if wld ==  "1": return opp+"2"
		return opp+"1" 
		


points = 0
for battle in data:
	actions = battle.replace("X","1").replace("Y","2").replace("Z","3") \
	.replace("A","1").replace("B","2").replace("C","3").replace(" ","")
	print(actions)
	actions = solver(actions[0],actions[1])
	points = points + int(actions[1])
	if actions[0] == actions[1]:
		points = points + 3
	if (actions[1] == "1" and actions[0] == "3") or \
	(actions[1] == "2" and actions[0] == "1") or \
	(actions[1] == "3" and actions[0] == "2"):
			points = points + 6	


print("Part 2:",points)
print("Execution Time:",str((time()-start)*1000),"ms")

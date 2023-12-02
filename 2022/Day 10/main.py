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

cycle_counter = 0
r_x = 1
signal_strength = 0

def cycle():
	global cycle_counter
	global r_x
	global signal_strength
	cycle_counter = cycle_counter + 1
	#print(cycle_counter)
	if cycle_counter in [20,60,100,140,180,220]:
		signal_strength = signal_strength + (cycle_counter * r_x)

for line in data:
	command = line.split(" ")
	if command[0] == "noop":
		cycle()
	elif command[0] == "addx":
		cycle()
		cycle()
		#print("R_X being incremented from",r_x)
		r_x = r_x + int(command[1])
		#print("new R_X",r_x)


print("Part 1:",signal_strength)

cycle_counter = 0
r_x = 1
signal_strength = 0
screen = []
def cycle():
	global cycle_counter
	global r_x
	global screen
	if r_x - 1 == cycle_counter or r_x == cycle_counter or r_x + 1 == cycle_counter:
		screen.append('#')
	else:
		screen.append(".")
	if cycle_counter == 39:
		cycle_counter = 0
	else:
		cycle_counter = cycle_counter + 1
	#print(screen)

for line in data:
	command = line.split(" ")
	if command[0] == "noop":
		cycle()
	elif command[0] == "addx":
		cycle()
		cycle()
		#print("R_X being incremented from",r_x)
		r_x = r_x + int(command[1])
		#print("new R_X",r_x)


for i in range(0, len(screen), 40):
    x = i
    print(''.join(screen[x:x+40]))
###..#....###...##..####.###...##..#....
#..#.#....#..#.#..#.#....#..#.#..#.#....
#..#.#....#..#.#..#.###..###..#....#....
###..#....###..####.#....#..#.#....#....
#....#....#....#..#.#....#..#.#..#.#....
#....####.#....#..#.#....###...##..####.


print("Part 2:",ans)
print("Execution Time:",str((time()-start)*1000),"ms")

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

dir_struct = {"/":{"files":[],"total_size":0}}
current_loc = []

for line in data:
	print(line)
	if line[0] == "$":
		if line[2:4] == "cd":
			if line[5:7] == "..":
				print("cd up one")
				current_loc.pop()
				print(current_loc)
			else:
				print("cd command")
				if current_loc == "":
					dir_struct["/"] = {}
				current_loc.append(line[5:])
				folder = dir_struct[current_loc[0]]
				for dir in current_loc[1:]:
					if dir not in folder:
						folder[dir] = {"files":[],"total_size":0}
					folder = folder[dir]
				print(current_loc)
		if line[2:4] == "ls":
			print("ls command")
	elif line[0:4] == "dir ":
		print("dir result")
	else:
		print("file result")
		folder = dir_struct[current_loc[0]]
		folder["total_size"] = folder["total_size"] + int(line.split(" ")[0])
		for dir in current_loc[1:]:
			if dir not in folder:
				folder[dir] = {}
			folder = folder[dir]
			folder["total_size"] = folder["total_size"] + int(line.split(" ")[0])
		folder["files"].append(int(line.split(" ")[0]))

print(dir_struct)
print(json.dumps(dir_struct,sort_keys=True, indent=4))

def dict_walker(dict_obj):
	for key, value in dict_obj.items():
		if isinstance(value,dict):
			for pair in dict_walker(value):
				yield(key,*pair)
		else:
			yield(key,value)

ans = 0
pairs = dict_walker(dir_struct)
for pair in pairs:
	if pair[-2] == "total_size":
		if pair[-1] < 100000:
			ans = ans+pair[-1]

print("Part 1:",ans)


total_disk = 70000000
unused_req = 30000000
pairs = dict_walker(dir_struct)

for pair in pairs:
	if pair[-2] == "total_size":
		if pair[-3] == "/":
			current_used = pair[-1]

min_to_free = unused_req - (total_disk-current_used)

print("Total_disk",total_disk)
print("unused_req",unused_req)
print("current_used",current_used)
print("current unused",total_disk-current_used)
print("min to free",unused_req - (total_disk-current_used))

del_options = []
sizes = []

pairs = dict_walker(dir_struct)
for pair in pairs:
	if pair[-2] == "total_size":
		print(pair)
		if pair[-1] >= min_to_free:
			del_options.append(pair)
			sizes.append(pair[-1])

p2ans = del_options[sizes.index(min(sizes))][-1]
print(p2ans)
print(del_options)


print("Part 2:",p2ans)
print("Execution Time:",str((time()-start)*1000),"ms")

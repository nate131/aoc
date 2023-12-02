import csv
import os
print(os.path.dirname(os.path.realpath(__file__)))
with open(os.path.dirname(os.path.realpath(__file__))+'/input.txt', 'r') as f:
    content = [line.rstrip() for line in f]

seatIDs = []

for boarder in content:
    row = boarder[:7].replace("F","0").replace("B","1")
    col = boarder[-3:].replace("L","0").replace("R","1")
    seatIDs.append((int(row,2)*8)+int(col,2))

seatIDs.sort()
print("Max SeatID:",max(seatIDs))
for a in range(1,len(seatIDs)):
    if seatIDs[a] - seatIDs[a-1] == 2:
        print("My SeatID:",seatIDs[a]-1)



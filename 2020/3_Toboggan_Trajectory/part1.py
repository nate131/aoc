import csv
import os
print(os.path.dirname(os.path.realpath(__file__)))
with open(os.path.dirname(os.path.realpath(__file__))+'/input.txt', 'r') as f:
    content = [line.rstrip() for line in f]

pos_x = 0
pos_y = 0
counter = 0
i = 0
while i < 1000:
    i += 1
    pos_x += 3
    if pos_x >= len(content[0])-1:
        pos_x = pos_x % len(content[0])
    pos_y += 1
    try:
        if content[pos_y][pos_x] == '#':
            counter += 1
    except Exception:
        break

print(counter)...#.....##.
.#..#.#..........#.##.....#.#..
.#...#...###..#..#..####.#...#.
##..............#..#.#...###..#
.#..#.#.#...#..#...#..#........
..#.#......#.#..##...#.#..#....
...#.#.....#.##..#...#..#......
...#...##....##..#....#..#...#.
#......##.#.......#...#..#.#...
.#..#......####...#............
...#..##.#...#....#.#.#.#......
....##...........##.#.#...##...
#.##.###........#..###.#..##...
....#......#....##...##.#......
#.............#...#.........#..
..##.......#.......#.#...#...#.
...#....####...#...#....#.###..
...##......#...###.#...#....#..
...#.............#...#.......#.
...#..#.##.##.#..#.##.#..#....#
..####.....#..#............#...
##....##..#.#.#.#..#..#.....#..
......##...##......#.#.........
#.#............#.#.#..#......#.
...#.#.#.....#..#..#.#..##.....
.#.#.............###..#....##..
....#.###..#..#.....#..#.##....
..#.#....#.......#.......##..#.
.#.##.#.#..#..##.........##....
...#...###.##....#####.......#.
......#.....##...##...#....#.#.
###.......##..#.....#......#.#.
...#..#..#....#.#.....##..#...#
..#....##.......#....#.........
#....##.........##......#.#..#.
#.....#.#.#..##..#.#.....##....
......#....#...#...#.###....##.
#...####...###.##..#.#.#..##...
......###....###..##......#..##
.#.####.###..#.....#...#..#...#
.###.#.....#..#.#..#.....##..##
...##...#.####....#......###...
...##.......#.#..#......#.#....
......##....#......#.........#.
............#....#............#
..#.#..........#......#..#.....
.#...#.#.#......#..##..#....##.
..##.#.#.#..#...###..#.#.##.#..
..#......#.........#.......#...
...#...##.#.##......#.....#....
..#.....#..##....#..##..#.#.##.
....##....#.#...#..##.##.##....
..#.............#...#......#...
.#.#.#.##..#.#..##...#.........
.##...........#..#.#........#..
.#..##.....#....#...#...#......
#.#.....##.#..#...######....#..
....#..#...##...#.........###..
..##.#...##..#......#.##..#...#
##..##...........#.......#.#...
.......##..##...###.##.......#.
.#.##...#.##...............#...
.......#.............#.......##
......#...........#...#..##....
.#..#..#....#..........#......#
...........#..#.....#....##....
###....#....##..#..##.....##...
#........#........#...#.##.##..
##.#.#........#..#.#..#.......#
.##.#.....#............#.......
.....#........#..##......##....
.#.####.#.##..................#
#...##.......#...#....#.#.##...
#.#.##...#.#......#.....#....#.
.........#....#...#....#.....#.
...#..#..#.#..#.##........##.#.
..#.##.#...#...#....#....##..#.
.#..#...####..........#.......#
....#...#...#...##.#.##......#.
.#....#...#.#..##..##.#.....#..
.....#....#......#.#####...###.
..#...##..#......#.#....#.....#
.##....##..###.#.....##.##.##..
#...#.#.........#....#....#....
...#.........#.##....##.#.#.#..
...#...#.#....#..#.#.......#.#.
#......#..#....##....#.........
...........#......#......###..#
#..#...#..##..#....#.....#.#.#.
#.#.....##..#..........###..#..
#...#.....#.......#..##...#....
...#....##.....#..##..#....#...
#...#.#......#..#...#........#.
.#....#...#...#.........##....#
..##...#.........#.......##..#.
......#.......#.....##....#..#.
.....##..#...#............#.#.#
...#....#.##..#...#.#....#.....
...#...........#.##....#..##.##
##......##....##...........#.#.
..##..##......#...#.##.##..#...
.#..##.#...##...#......###.##.#
###.#....##..#..#.##..##...##..
..#........##.#...#.......#....
.....##....##.#.###.....#....#.
#.##....#....##.....#..#.#.....
#.........#..##...##.......##..
.#....#......#.#...##..........
##..##.....##....###..#...#.#.#
..##.#.#..#......#.#....###..#.
.#.##.....##.......##.#.##..#..
..##...#........#.#.#.##.#..###
........#.......#...##....#.#..
...#..#...#.##..#...#.#.###.##.
..#.#....#..#...#..##.........#
#....#..##..##....#.........#..
.......#.......#....#....#.#...
...#.##...#...#..#....#.###.##.
##.##...#..........#....#......
#.##.#.....#..#............##.#
.##...#.#.#.##...........#..##.
.#...#....#.......##...##...#.#
.#......#..#...#...#....#.#....
...#..#..#...#..##..##.....#..#
.#.##..#.#...#..#.#...#...#...#
#.##..........#.##..#....#.....
##....#.#..........#..#....#...
..#..##.#.......#...#.##......#
....##......#......#.#.#.##....
###......#...##..#..........###
##.#.##.....###.#..#.#......#..
#.#.#........#..........#....#.
...#.#..#.......#......##.#....
......#.....#.#.#....###..#...#
.........#...#..#####..#.#..#..
..........#.#.#####.#..#.....#.
....#.......#.#....#.....##..#.
#...##.#..#.#........#.#..#..##
#......#..#.#.....##......#.##.
.##...#....#.##..#.....###..#..
#....#.#..##....##..#.#####....
.......##..........#......#....
......#.#...#............#.....
.......###.....##.#..#.#....#.#
...#...#..........#....##...##.
.#..#.#.#....#.#.....##..#.#..#
......#.#..#....#..#...#.......
##.#####............#.#.####.#.
#.....###.#.......##...###....#
......#.##..##.........#.#.....
.#.#......#..#.##......#......#
.#.#.#..#.#...##.....#..#.#..#.
.#.#....#......................
#.#..###...#...####.##.#....#.#
.....#............#....#..#.##.
#..#...#.#....#....#..#..#...#.
...#.......#..#.#....#.......#.
.#..#.#...#.#.####..#...#....##
....#..#..............####....#
.....#.#.###....#.#.#.#...#....
..####..#.#.##.##.##....#..#...
.#.#.#.###..#.##..............#
..#.#..#...#.....#.......#.##..
.#.#..#.....##...###.....#..#..
..#..#......#.##..#......##..#.
.....#.#.#..##..###.#..........
.##......#...#.##.......#..#..#
.......#...#.....###.##...##...
..##..#.#.......#..............
#.....#......#.#..#..#..#......
..###.......##...#.##....#.....
.....##...........##.....#...##
.#.#.####....###.#.......#...##
#.#..##.#.#.....#.#....#.......
.........#.#..#...............#
..##.#..#..#####.###.........#.
.#........#...#...#...#.##.#..#
.#.##..........#..##....#.#.#..
.##......#....#.#....##.#.#.#..
.......##.####..#..#.#..#.#...#
...#.....#..##..###.#..##...#..
#.......##..#####....#.......#.
#.#.##.................#...###.
................####...........
.#..#......#...###.............
......#.#.##.##.....#..........
.......#..#.#............##....
#........#..#....#......#.####.
...#.#....##..#..#.............
..#.#......#...#.#..#..........
###...###...........#......#...
#.###..###........###...#..###.
.#.....#...#.#...........##....
....#..##.....#..#......#......
#.###.#........#.#.##..........
#.#.#.#.#..#.#...#...##.#......
..###.......###..#.#.#.#.#.....
...#........#.......#.###..##..
.#........#...#.#........#..##.
#.......###..#....##.###...#..#
.##....###..##...........##...#
#...#..........#.....#..##..#..
#..##..#..##.#.........##......
..#.#..###..###.....#.......#..
#...#...........##.#.#.###.....
...#....#.....#.....#.##.#.##.#
...........##.......####...#..#
#.#...#..##..#.#..#..........#.
..#...#.##........#.#..........
.##.....#.#.#....#.#.......#.#.
.......#.##...#.##....#.#...#..
......#...##...###...#.....###.
##......#.##.####.##...##......
..#....#.#..###.#..##....#..#..
...##..###.....###.....#.......
...#.....#.#........#..#..##.#.
.....................#.....#.#.
.#...#...##.#..#..........#...#
#.....#..#....#..#.......####..
.##.......##......###.#..#...##
.#.##..#...#..........##.......
...##...........##..##......#..
#....##.##...#......##.#.##.##.
..##.##.#.#.#....#........#.#..
....#......#......##..##.#.#...
.............#.##...#..#...#...
.#..#...#.........#...........#
....#.....#..................#.
........##............#...#..##
.###.....##...#...#.##.....##..
...##.#.........##.#.#..#......
#...........##.#..#........#..#
....#....#..##.#..##..#..#..#.#
#..##..#............#...#.#.#..
#......#..##......#...##..#...#
....#.#..##.#.#...####...#.....
.##..#..##....#...#....#...##.#
##.....#.#........#....#.#.#...
......#.#...##....#.###.....#.#
..#..#............###.###.##.#.
#..#.##.##.##..#...#.#.##..#...
....#..#.#...#......#..###.....
.#........#...###.....#...#....
....##.##....#..#...#.#####.#.#
...#..#...#.#.....#....#...###.
..........####...##............
.....#....##...##......#..#...#
..#...#.####......#...#..#..###
.#.....#....#..#...###..#.#....
..#..#......#.#...#.....##....#
.....##....#....#...#.....##...
#............##.#....#.#.#..#..
#......#......#....#.#..##.#...
#.#......##.....#.#..##.#.#....
.#.###..#.#......##...........#
#.#.........##..#.#.##......#..
##....####...##...........#....
....###.#..##.#.#.##...##.....#
..###.......##.......#......#..
..#.###.##.#...................
...#.#...#..#..#..##.###...#.#.
#...#..#...#..#....#..#...#....
....#........#.#.#.##.##.#..#.#
...#....#.#...#..#....#.#.#....
..#...#..##.#....##...###...##.
#......#.....#.....#....####.#.
...##.#..#.#.....#..#..##.#....
.####.#..#...#.#......#......#.
..#.#....#..#..##.#......##....
....#...#.#..#...#...##........
##..#.#....#..#.........#..##..
...#.......#....#..##...###..##
#......##.#..#..#..#..###.#.###
.#..##.#...##...#.............#
###.........#...###.#.#..#....#
.#.....#..#........#.#.......#.
#..#.#.....#.........###..#....
#..##.....#.#....#.###.....#..#
....#..#.......##..#.#..##....#
##.##..#....#..#.#.###.........
..##....#........#..#..#.##.#.#
.#....#...##..#.#.....#..##..#.
#..#.......#......#...#...#.##.
...##.#......#.#..#......#.....
......#...#.##.#....#...#.##.#.
#.....#..#.#.#...##...#........
....#.#..#.#.....#....#.#..#...
....#.#...###............#.....
.#.#...##.......#....#.##...#.#
.....#.##......#.#..#...#....#.
.###....#...#........#.........
..#.....#..#.#.#..##...#..#....
...###..#....#.....#.........##
#....#....###...#.#............
.#..##.....#...........#.#..#..
..#.#.#.......##..#.#..........
.#...#...####.#...#####.....#.#
..#....##.....#..#...#.........
#.#......#.##.........#......##
..#.#...#.##..#....#....#.##...
#....#......##.#..#......#.#.#.
#.#.............##..#.#........
..#.###.......##.....##.#..##.#
.........#........#...#..#....#
.........##.#.#..#..#....#....#
##..#..#.#.....##.........#.#.#
..##.##..#.##..........##.#..#.
...#..#####.......#.........#..
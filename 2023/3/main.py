import time
start_time = time.time()

#my_file = open("sample.txt", "r") 
#my_file = open("sample2.txt", "r") 
my_file = open("input.txt", "r")
data = my_file.read()
input_val = data.split("\n")
my_file.close()

#print(input_val)

symbols = "1234567890."
answers = []
part_2_ans = []

def part_1():
    current_num = []
    for x,line in enumerate(input_val):
        isvalid = False
        for y,char in enumerate(line):
            #print(x,y,char)
            if input_val[x][y].isnumeric():
                current_num.append(input_val[x][y])
                if isvalid == False:
                    isvalid = check_symbol(x,y,input_val)
            if (input_val[x][y] == "." or input_val[x][y] not in symbols and len(current_num) > 0) or (y+1 == len(line) and len(current_num) > 0):
                if isvalid:
                    answers.append(int("".join(current_num)))
                current_num = []
                isvalid = False


def check_symbol(x,y,input_val):
    #print("Checking for position",x,y)
    for x1 in range(x-1,x+2,1):
        for y1 in range(y-1,y+2,1):
            if x1 >= 0 and y1 >= 0 and x1 < len(input_val) and y1 < len(input_val[0]):
                #print(x1,y1)
                #print("checking if ",x1,y1,input_val[x1][y1]," is part of ",symbols)
                if input_val[x1][y1] not in symbols:
                    #print("Is Valid Record")
                    return True
    #print("Is NOT Valid Record")
    return False

def part_2():
    for x,line in enumerate(input_val):
        for y,char in enumerate(line):
            if input_val[x][y] == "*":
                part_2_ans.append(get_adjacent(x,y,input_val))

def get_adjacent(x,y,input_val):
    gears = []
    for x1 in range(x-1,x+2,1):
        already_tested = []
        for y1 in range(y-1,y+2,1):
            if y1 not in already_tested:
                current_number = []
                if x1 >= 0 and y1 >= 0 and x1 < len(input_val) and y1 < len(input_val[0]):
                    if input_val[x1][y1].isnumeric():
                        y2 = y1
                        while y2 >=0 and y2 < len(input_val[0]) and input_val[x1][y2].isnumeric():
                            already_tested.append(y2)
                            y2 = y2 - 1
                        y2 = y2 + 1
                        while y2 >=0 and y2 < len(input_val[0]) and input_val[x1][y2].isnumeric():
                            already_tested.append(y2)
                            current_number.append(input_val[x1][y2])
                            y2 = y2 + 1
                        gears.append(int("".join(current_number)))
                        current_number = []
    if len(gears) == 2:
        return (gears[0] * gears[1])
    else:
        return 0
    print(gears)



part_1()
print("Part 1:",sum(answers))
part_2()
print("Part 2:",sum(part_2_ans))

print("--- %s seconds ---" % (time.time() - start_time))

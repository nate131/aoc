import time
start_time = time.time()

#my_file = open("sample.txt", "r") 
#my_file = open("sample2.txt", "r") 
my_file = open("input.txt", "r")
data = my_file.read()
input_val = data.split("\n")
my_file.close()


def part_1():
    answers = []
    entries = []
    for card in input_val:
        entries.append(card[9:].replace("  "," ").split("|"))
    for entry in entries:
        winning = entry[0].strip().split(" ")
        numbers = entry[1].strip().split(" ")
        points = len([i for i in numbers if i in winning ])
        if points > 0:
            #print(winning,numbers,points,1*2**(points-1))
            answers.append(1*2**(points-1))
    print(sum(answers))


def part_2():
    answers = []
    entries = []
    for card in input_val:
        entries.append(card[9:].replace("  "," ").split("|"))
    for entry in entries:
        winning = entry[0].strip().split(" ")
        numbers = entry[1].strip().split(" ")
        points = len([i for i in numbers if i in winning ])
        answers.append([points,1])
    #print(answers)
    for i,ans in enumerate(answers):
        #print("POS:",i)
        if ans[1] > 0:
            for k in range(0,ans[1]):
                for j in range(i+1,i+ans[0]+1):
                    if j < len(answers):
                        answers[j][1] = answers[j][1] + 1
        #print(answers)
    print(sum([el[1] for el in answers]))

part_1()
part_2()
print("--- %s seconds ---" % (time.time() - start_time))

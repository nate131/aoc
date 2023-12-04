import re

#my_file = open("sample.txt", "r") 
#my_file = open("sample2.txt", "r") 
my_file = open("input.txt", "r")
data = my_file.read()
input_val = data.split("\n")
my_file.close()


#AOC Work
answers = []

for i in input_val:
    first_digi = 0
    last_digi = 0
    for x in range(1,len(i)+1):
        if first_digi == 0:
            test_val = i[:x].replace('one','1').replace('two','2').replace('three','3').replace('four','4').replace('five','5').replace('six','6').replace('seven','7').replace('eight','8').replace('nine','9')[-1]
            if test_val.isnumeric():
                first_digi = test_val
    for x in range(len(i)-1,-1,-1):
        if last_digi == 0:
            test_val = i[x:].replace('one','1').replace('two','2').replace('three','3').replace('four','4').replace('five','5').replace('six','6').replace('seven','7').replace('eight','8').replace('nine','9')[0]
            if test_val.isnumeric():
                last_digi = test_val
    answers.append(int(str(first_digi)+str(last_digi)))

print(sum(answers))

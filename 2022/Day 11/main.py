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
    data = fd.read().split('\n\n')  # list
    #data = [[int(number) for number in split_data.split('\n')] for split_data in fd.read().split('\n\n')] # int-list of lists
ans = ""

class Monke:
    def __init__(self, monke, items, operation, test, true_monke, false_monke):
        self.monke = monke
        self.items = items
        self.operation = operation
        self.test = test
        self.true_monke = true_monke
        self.false_monke = false_monke
        self.inspect_count = 0

    def __str__(self):
        return f"{self.monke}({self.items})"

    def turn(self):
        global monkes
        #print("Monkey "+self.monke+":")
        #for each item in order inspect & throw
        test_items = self.items.copy()
        for idx, item in enumerate(test_items):
            self.inspect_count  = self.inspect_count + 1
            #print("  Monkey inspects an item with a worry level of "+str(item)+".")
            #perform self.operation on item
            old = item
            new = eval(self.operation)
            #print("    Worry level is "+self.operation+" to "+str(new)+".")
            #divide by 3 (round down)
            new = new//3
            item = new
            #print("    Monkey gets bored with item. Worry level is divided by 3 to "+str(new)+".")
            #perform validation
            if new % self.test == 0:
                #print("    Current worry level is divisible by "+str(self.test)+".")
                #if on throw
                self.items.pop(0)
                monkes[self.true_monke].items.append(item)
                #print("    Item with worry level "+str(item)+" is thrown to monkey "+str(self.true_monke)+".")
            else:
                #print("    Current worry level is not divisible by "+str(self.test)+".")
                #if on throw
                self.items.pop(0)
                monkes[self.false_monke].items.append(item)
                #print("    Item with worry level "+str(item)+" is thrown to monkey "+str(self.false_monke)+".")


monkes = []
for line in data:
    attr = line.split('\n')
    monke = attr[0].split(" ")[1][:-1]
    items = [int(i) for i in attr[1].split(":")[1].split(",")]
    operation = attr[2].split("=")[1].strip()
    test = int(attr[3].split(" ")[-1])
    true_monke = int(attr[4].split(" ")[-1])
    false_monke = int(attr[5].split(" ")[-1])
    monkes.append(Monke(monke,items,operation,test,true_monke,false_monke))
    print(monke,items,operation,test,true_monke,false_monke)

for i in range(20):
    #print("Round",i)
    for monke in monkes:
        monke.turn()
    #for monke in monkes:
    #    print(monke)

inspects = []
for monke in monkes:
    inspects.append(monke.inspect_count)

inspects.sort(reverse=True)

print("Part 1:",math.prod(inspects[:2]))




class Monke:
    def __init__(self, monke, items, operation, test, true_monke, false_monke):
        self.monke = monke
        self.items = items
        self.operation = operation
        self.test = test
        self.true_monke = true_monke
        self.false_monke = false_monke
        self.inspect_count = 0

    def __str__(self):
        return f"{self.monke}({self.items})"

    def turn(self,magic):
        global monkes
        test_items = self.items.copy()
        for idx, item in enumerate(test_items):
            self.inspect_count  = self.inspect_count + 1
            old = item
            new = eval(self.operation )
            item = new
            if new % self.test == 0:
                self.items.pop(0)
                if item > magic:
                    monkes[self.true_monke].items.append(item % magic)
                else:
                    monkes[self.true_monke].items.append(item)
            else:
                self.items.pop(0)
                monkes[self.false_monke].items.append(item)




monkes = []
for line in data:
    attr = line.split('\n')
    monke = attr[0].split(" ")[1][:-1]
    items = [int(i) for i in attr[1].split(":")[1].split(",")]
    operation = attr[2].split("=")[1].strip()
    test = int(attr[3].split(" ")[-1])
    true_monke = int(attr[4].split(" ")[-1])
    false_monke = int(attr[5].split(" ")[-1])
    monkes.append(Monke(monke,items,operation,test,true_monke,false_monke))
    print(monke,items,operation,test,true_monke,false_monke)

turn_limit = 10001

inspect_checker = []
diff_checker = []

tests = []
for monke in monkes:
    tests.append(monke.test)
print(1%19)
for x in range(1,10000000):
    failed = False
    for test in tests:
        if x % test != 0:
            failed = True
            continue
    if failed:
        continue
    print("a magic number is",x)
    magic_num = x


for i in range(1,turn_limit):
    #print("Round",i)
    for monke in monkes:
        monke.turn(magic_num)
    if i == 20 or i == 1000 or i == 1:
        print("== After round "+str(i)+" ==")
        inspects = []
        for monke in monkes:
            print("Monkey "+str(monke.monke)+" inspected items "+str(monke.inspect_count)+" times. ")

print("------------------")

inspects = []
for monke in monkes:
    print("Monkey "+str(monke.monke)+" inspected items "+str(monke.inspect_count)+" times. ")
inspects = []
for monke in monkes:
    inspects.append(monke.inspect_count)

inspects.sort(reverse=True)

inspects.sort(reverse=True)





print("Part 2:",math.prod(inspects[:2]))
print("Execution Time:",str((time()-start)*1000),"ms")

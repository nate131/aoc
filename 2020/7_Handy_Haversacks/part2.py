import csv
from collections import Counter
import os
import re
print(os.path.dirname(os.path.realpath(__file__)))
with open(os.path.dirname(os.path.realpath(__file__))+'/input.txt', 'r') as f:
    content = f.read().split("\n")
clean_rules = {}

for rule in content:
    rule_base = rule.split(" bags contain ")
    #print(rule_base[1])
    rule_set = re.findall(r"((\d+).(\w+ \w+)|no)",rule_base[1])
    #print(rule_set)
    if rule_set[0] == "no other bags":
        clean_rules.update(rule_base[0])
    else:
        bags = {}
        for match in rule_set:
            bags.update({match[2]: match[1]})
        clean_rules.update({rule_base[0]: bags})
    #print(rule_set)


def bag_counter(bag,clean_rules,counter=0):
    print("Searching:",bag, clean_rules[bag])
    for a in clean_rules[bag]:
        if clean_rules[a] == {'':''}:
            print("no bags allowed inside", a)
            counter += int(clean_rules[bag][a])
            continue
        else:
            print(bag," contains ",clean_rules[bag][a], a,"Total Count: ",counter)
            counter += int(clean_rules[bag][a]) + (int(clean_rules[bag][a]) * bag_counter(a,clean_rules,0))
    return counter


print(bag_counter("shiny gold",clean_rules))
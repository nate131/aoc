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

def rule_search(bag,clean_rules):
    for a in clean_rules[bag]:
        if clean_rules[bag][a] == "":
            #print("no bags allowed inside", bag)
            continue
        if a == "shiny gold":
            return True
        else:
            if rule_search(a,clean_rules) : return True
    return False
counter = 0
for bag in clean_rules:
    if rule_search(bag,clean_rules): counter +=1

print(counter)
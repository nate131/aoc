import csv
import os
print(os.path.dirname(os.path.realpath(__file__)))
with open(os.path.dirname(os.path.realpath(__file__))+'/input.txt', 'r') as f:
    content = [line.rstrip() for line in f]

counter = 0
clean_input = {}
for line in content:
    if not clean_input.get(counter) : clean_input[counter] = {}
    if line == "":
        counter += 1
        continue
    print(line,counter)
    split_line = line.split(" ")
    for split in split_line:
        chunk = split.split(":")
        clean_input[counter][chunk[0]] = chunk[1]

print(clean_input)

valid = 0
for customer in clean_input.values():
    print(customer)
    if customer.get("byr") and customer.get("iyr") and customer.get("eyr") and customer.get("hgt") and customer.get("hcl") and customer.get("ecl") and customer.get("pid"):
        valid += 1

print(valid)
import csv
import os
import re

print(os.path.dirname(os.path.realpath(__file__)))
with open(os.path.dirname(os.path.realpath(__file__))+'/input.txt', 'r') as f:
    content = [line.rstrip() for line in f]

counter = 0
clean_input = {}
for line in content:
    if not clean_input.get(counter) : clean_input[counter] = {}
    if line == "":
        clean_input[counter] = dict(sorted(clean_input[counter].items()))
        counter += 1
        continue
    print(line,counter)
    split_line = line.split(" ")
    for split in split_line:
        chunk = split.split(":")
        if chunk[0] != "cid":
            clean_input[counter][chunk[0]] = chunk[1].strip()



print(clean_input)

valid = 0
has_fields = 0
colour_re = re.compile("#[0-9a-f]{6}")
pid_re = re.compile("^[0-9]{9}$")

for customer in clean_input.values():
    if customer.get("byr") and customer.get("iyr") and customer.get("eyr") and customer.get("hgt") and customer.get("hcl") and customer.get("ecl") and customer.get("pid"):
        has_fields += 1
        if int(customer.get("byr")) < 1920 or int(customer.get("byr")) > 2002:
            #print(customer)
            #print(customer.get("byr"), "byr <1920 or >2002")
            continue
        if int(customer.get("iyr")) < 2010 or int(customer.get("iyr")) > 2020:
            #print(customer)
            #print(customer.get("iyr"), "iyr <2010 or >2020")
            continue
        if int(customer.get("eyr")) < 2020 or int(customer.get("eyr")) > 2030:
            #print(customer)
            #print(customer.get("eyr"), "eyr <2020 or >2030")
            continue
        if customer.get("hgt")[-2:] == "cm" and (int(customer.get("hgt")[0:-2]) < 150 or int(customer.get("hgt")[0:-2]) > 193):
            #print(customer)
            #print(customer.get("hgt"), "hgt is CM but <150 or >193")
            continue
        if customer.get("hgt")[-2:] == "in" and (int(customer.get("hgt")[0:-2]) < 59 or int(customer.get("hgt")[0:-2]) > 76):
            #print(customer)
            #print(customer.get("hgt"), "hgt is in but <59 or >76")
            continue
        if customer.get("hgt")[-2:] != "in" and customer.get("hgt")[-2:] != "cm":
            #print(customer)
            #print(customer.get("hgt"), "hgt doesnt end in in or cm")
            continue
        if not colour_re.match(customer.get("hcl")):
            #print(customer)
            #print(customer.get("hcl"), "is not hex")
            continue
        if customer.get("ecl") != "amb" and customer.get("ecl") != "blu" and customer.get("ecl") != "brn" and customer.get("ecl") != "gry" and customer.get("ecl") != "grn" and customer.get("ecl") != "hzl"  and customer.get("ecl") != "oth" :
            #print(customer)
            #print(customer.get("ecl"), "is not amb blu brn gry grn hzl oth")
            continue
        if not pid_re.match(customer.get("pid")):
            #print(customer)
            #print(customer.get("pid"), "is not 9 digit")
            continue
        valid += 1
        print(customer)
        #print("Valid Data")
        
print(has_fields)
print(valid)
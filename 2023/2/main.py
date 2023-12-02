

#f = open('sample.txt') # Open file on read mode
f = open('input.txt') # Open file on read mode
lines = f.read().splitlines() # List with stripped line-breaks
f.close() # Close file

#print(lines) 

test = {"red": 12, "green": 13, "blue": 14}
answers = []
for line in lines:
    possible = True
    segments = line.split(":")
    #print(segments)
    game_num = int(segments[0].replace("Game ",""))
    #print(game_num)
    rounds = segments[1].split(";")
    for round in rounds:
        marble_sets = round.split(",")
        for marbles in marble_sets:
            items = marbles.strip().split(" ")
            #print(items)
            if int(items[0]) > test[items[1].strip()]:
                possible = False
    if possible:
        answers.append(game_num)
#print(answers)
print("Part 1:",sum(answers))


#####################################
# PART 2
#####################################
answers = []
for line in lines:
    possible = True
    segments = line.split(":")
    #print(segments)
    game_num = int(segments[0].replace("Game ",""))
    answers.append({"red": 0,"green": 0, "blue": 0})
    #print(game_num)
    rounds = segments[1].split(";")
    for round in rounds:
        marble_sets = round.split(",")
        for marbles in marble_sets:
            items = marbles.strip().split(" ")
            #print(items)
            if int(items[0]) > answers[game_num-1][items[1].strip()]:
                print(game_num, "Updating",items[1].strip(), "from", answers[game_num-1][items[1].strip()],"to", int(items[0]))
                answers[game_num-1][items[1].strip()] = int(items[0])
prod_answer = []
for item in answers:
    prod_answer.append(item["red"] * item["green"] * item["blue"])
print(answers)
print(prod_answer)
print(sum(prod_answer))
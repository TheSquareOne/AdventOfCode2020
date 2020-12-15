import os

def readInput(filename):

    rules = dict()
    with open(os.path.join(os.path.dirname(__file__), filename), 'r') as file:
        input = file.readlines()
        for line in input:
            line = line.split(' bags contain')
            rules.update({
                line[0]:
                line[1].strip(' \n.')
            })
    return rules


def findBag(rules, bag):

    okBags = []
    for i in rules.items():
        if bag in i[1]:
            okBags.append(i[0])

    for i in okBags:
        for y in rules.items():
            if (i in y[1]) and (y[0] not in okBags):
                okBags.append(y[0])

    return okBags


def countBags(rules, bag):

    bags = list(map(str.strip, rules.get(bag).split(',')))

    if bags[0] == 'no other bags':
        return 0

    amount = 0
    while bags:

        x = bags.pop().split(' ', 1)

        if 'bags' in x[1]:
            x[1] = x[1].replace(' bags', '')
        elif 'bag' in x[1]:
            x[1] = x[1].replace(' bag', '')

        amount += int(x[0]) + int(x[0]) * countBags(rules, x[1])

    return amount


# Puzzle input
rules = readInput('puzzle_input.txt')

# Part 1
okBags = findBag(rules, 'shiny gold')
for bag in okBags:
    print(bag)
print("Total of", len(okBags), "different bag, can contain your bag.")

# Part 2
print("Your bag must contain:", countBags(rules, 'shiny gold'), "bags!")

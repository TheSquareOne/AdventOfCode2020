import os
from itertools import combinations

def readData(filename):
    with open(os.path.join(os.path.dirname(__file__), filename), 'r') as file:
        data = list(map(str.strip, file.readlines()))
    return data


def findWeakness(data):
    for i in range(26 - 1, len(data)):
        preamble = []
        for y in range(i - 25, i):
            preamble.append(int(data[y]))

        if int(data[i]) not in map(sum, combinations(preamble, 2)):
            print('Weakness found in line', i + 1, ',', data[i])
            return data[i]


data = readData('puzzle_input.txt')

# Part 1
findWeakness(data)

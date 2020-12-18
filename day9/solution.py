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
            return int(data[i])


def findContiguousSet(data, invalidNum):
    s = []
    for i in range(0, len(data) - 1):
        for y in range(i, len(data)):
            s.append(int(data[y]))

            if sum(s) > int(invalidNum):
                s.clear()
                break
            elif sum(s) == int(invalidNum):
                print('Contiguous set for invalid number found from line',
                    i, 'to', y)
                print('Highest number being:', max(s))
                print('Smallest number being:', min(s))
                print('Addition of highest and smallest is:',
                    max(s) + min(s))
                return min(s) + max(s)


data = readData('puzzle_input.txt')

# Part 1
invalidNum = findWeakness(data)

# Part 2
invalidSum = findContiguousSet(data, invalidNum)

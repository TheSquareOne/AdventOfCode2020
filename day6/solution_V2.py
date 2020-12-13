import os

def readInput(filename):

    with open(os.path.join(os.path.dirname(__file__), filename), 'r') as file:
#        input = (line.strip() for line in file.readlines())
        input = []
        tempList = []

        for line in file.readlines():
            if line == '\n':
                input.append(tempList)
                tempList = []
            else:
                tempList.append(line.strip())
        else:
            input.append(tempList)

    return input


def countYes(input, solution = 1):

    sum = 0

    if solution == 1:
        for group in input:
            for c in range(ord('a'), ord('z') + 1):
                for person in group:
                    if chr(c) in person:
                        sum += 1
                        break

        return sum

    elif solution == 2:
        for group in input:
            for c in range(ord('a'), ord('z') + 1):
                for person in group:
                    if chr(c) in person:
                        continue
                    else:
                        break
                else:
                    sum += 1
        return sum

    else:
        print("No such solution, use 1 or 2!")
        return -1


input = readInput('group_answers.txt')
print("Solution part 1 answer:", countYes(input, 1))
print("Solution part 2 answer:", countYes(input, 2))

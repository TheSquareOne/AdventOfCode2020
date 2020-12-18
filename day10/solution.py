import os

def readSpecs(filename):
    with open(os.path.join(os.path.dirname(__file__), filename), 'r') as file:
        adapters = list(map(int, file.readlines()))
    return adapters


def chainAdapters(adapters):
    diffs = {'one': 0, 'two': 0, 'three': 0}

    adapters.append(0)                      # Add outlet
    adapters.append(max(adapters) + 3)      # Add build-in adapter
    adapters.sort()

    for i in range(0, len(adapters) - 1):
        if (adapters[i + 1] - adapters[i]) == 3:
            diffs['one'] += 1
        elif (adapters[i + 1] - adapters[i]) == 2:
            diffs['two'] += 1
        elif (adapters[i + 1] - adapters[i]) == 1:
            diffs['three'] += 1
        else:
            print('Invalid adapter')

    return diffs


adapters = readSpecs('joltage_output.txt')

# Part 1
diffs = chainAdapters(adapters)
print(diffs['one'], '\t1-jolt differences,')
print(diffs['two'], '\t2-jolt differences,')
print(diffs['three'], '\t3-jolt differences,')
print('1 and 3 differences multiplied:', diffs['one'] * diffs['three'])

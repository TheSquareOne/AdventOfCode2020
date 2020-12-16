import os


def readCode(filename):
    with open(os.path.join(os.path.dirname(__file__), filename), 'r') as file:
        bootCode = file.readlines()
    return bootCode


def findLoop(bootCode):

    acc = 0
    i = 0
    usedInst = []

    while i < len(bootCode):

        cmd, arg = bootCode[i].strip().split(' ')

        # Keep list of used instructions
        if i not in usedInst:
            usedInst.append(i)
        else:
            return acc

        # Commands
        if cmd == 'acc':
            acc += int(arg)
        elif cmd == 'jmp':
            i += int(arg)
            continue
        elif cmd == 'nop':
            pass

        i += 1


bootCode = readCode('boot_code.txt')

# Part 1
print('Part 1 acc is',findLoop(bootCode))

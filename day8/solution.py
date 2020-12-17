import os


def readCode(filename):
    with open(os.path.join(os.path.dirname(__file__), filename), 'r') as file:
        bootCode = file.readlines()
    return bootCode


def getAcc(bootCode):

    acc = 0
    i = 0
    usedInst = []

    while i < len(bootCode):

        cmd, arg = bootCode[i].strip().split(' ')

        # Keep list of used instructions
        if i not in usedInst:
            usedInst.append(i)
        else:
            return -1, acc

        # Commands
        if cmd == 'acc':
            acc += int(arg)
        elif cmd == 'jmp':
            i += int(arg)
            continue
        elif cmd == 'nop':
            pass

        i += 1

    return 0, acc


def fixBootCode(bootCode):
    i = 0
    while i < len(bootCode):

        bootCode_copy = bootCode.copy()
        cmd, arg = bootCode_copy[i].strip().split(' ')

        if cmd == 'jmp':
            bootCode_copy[i] = bootCode_copy[i].replace('jmp', 'nop')
        elif cmd == 'nop' and arg != 0:
            bootCode_copy[i] = bootCode_copy[i].replace('nop', 'jmp')

        i += 1

        err, acc = getAcc(bootCode_copy)

        if err == 0:
            print('Instruction number', i, 'was causing the loop!')
            return acc


bootCode = readCode('boot_code.txt')

# Part 1
err, acc = getAcc(bootCode)
print('Part 1 acc is', acc)

# Part 2
acc = fixBootCode(bootCode)
print('Part 2 acc is', acc)

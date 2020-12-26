import os


def getInstructions(filename):
    with open(os.path.join(os.path.dirname(__file__), filename), 'r') as file:
        inst = list(map(str.strip, file.readlines()))
    return inst


def readInstructions(inst):
    directions = ['north', 'east', 'south', 'west']
    hori, verti = 0, 0
    curr_dir = 'east'

    i = 0
    while i < len(inst):
        dir, value = inst[i][:1], int(inst[i][1:])
        i += 1

        if dir == 'R':
            if (directions.index(curr_dir) + int(value / 90)) >= len(directions):
                curr_dir = directions[(directions.index(curr_dir) + int(value / 90)) - len(directions)]
            else:
                curr_dir = directions[directions.index(curr_dir) + int(value / 90)]
        elif dir == 'L':
            curr_dir = directions[directions.index(curr_dir) - int(value / 90)]
        elif dir == 'N':
            verti += value
        elif dir == 'S':
            verti -= value
        elif dir == 'E':
            hori += value
        elif dir == 'W':
            hori -= value
        elif dir == 'F':
            if curr_dir == 'north':
                verti += value
            elif curr_dir == 'east':
                hori += value
            elif curr_dir == 'south':
                verti -= value
            elif curr_dir == 'west':
                hori -= value

    return abs(hori) + abs(verti)


# Part 1
inst = getInstructions('nav_inst.txt')
manhDist = readInstructions(inst)
print(manhDist)

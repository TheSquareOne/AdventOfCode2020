import os
import copy


def readLayout(filename):
    with open(os.path.join(os.path.dirname(__file__), filename), 'r') as file:
        layout = list(map(list, map(str.strip, file.readlines())))
    return layout


def predictOccupancy(layout):

    next_occupancy = copy.deepcopy(layout)
    prev_occupancy = list()
    roundCount = 0
    while(prev_occupancy != next_occupancy):
        roundCount += 1
        prev_occupancy = copy.deepcopy(next_occupancy)

        for row in range(0, len(layout)):
            for col in range(0, len(layout[row])):

                adjacent = countAdjacent(prev_occupancy, row, col)

                if prev_occupancy[row][col] == 'L' and adjacent == 0:
                    next_occupancy[row][col] = '#'
                elif prev_occupancy[row][col] == '#' and adjacent >= 4:
                    next_occupancy[row][col] = 'L'

    print('Prediction finished after', roundCount, 'rounds!')
    return next_occupancy


def predictOccupancy_part2(layout):

    next_occupancy = copy.deepcopy(layout)
    prev_occupancy = list()
    roundCount = 0
    while(prev_occupancy != next_occupancy):
        roundCount += 1
        prev_occupancy = copy.deepcopy(next_occupancy)

        for row in range(0, len(layout)):
            for col in range(0, len(layout[row])):

                adjacent = countAdjacent(prev_occupancy, row, col)
                directions = countDirections(prev_occupancy, row, col)

                if prev_occupancy[row][col] == 'L' and adjacent == 0 and directions == 8:
                    next_occupancy[row][col] = '#'
                elif prev_occupancy[row][col] == '#' and directions < 4:
                    next_occupancy[row][col] = 'L'

    print('Prediction finished after', roundCount, 'rounds!')
    return next_occupancy


def countAdjacent(layout, row, col):
    count = 0
    for row2 in range(row-1, row+2):
        if row2 < 0 or row2 >= len(layout): continue

        for col2 in range(col-1, col+2):
            if col2 < 0 or col2 >= len(layout[row2]): continue

            if row2 == row and col2 == col:
                continue

            if layout[row2][col2] == '#':
                count += 1

    return count


def countOccupiedSeats(layout):
    count = 0
    for row in layout:
        for col in row:
            if col == '#':
                count += 1
    return int(count)


def countDirections(layout, row, col):

    count = 0

    # N
    for x in range(row-1, 0-1, -1):
        if layout[x][col] == '#':
            break
        elif layout[x][col] == 'L':
            count += 1
            break
    else:
        count += 1

    # S
    for x in range(row+1, len(layout)):
        if layout[x][col] == '#':
            break
        elif layout[x][col] == 'L':
            count += 1
            break
    else:
        count += 1

    # W
    for y in range(col-1, 0-1, -1):
        if layout[row][y] == '#':
            break
        elif layout[row][y] == 'L':
            count += 1
            break
    else:
        count += 1

    # E
    for y in range(col+1, len(layout[0])):
        if layout[row][y] == '#':
            break
        elif layout[row][y] == 'L':
            count += 1
            break
    else:
        count += 1

    # NW
    for x, y in zip(range(row-1, 0-1, -1), range(col-1, 0-1, -1)):
        if layout[x][y] == '#':
            break
        elif layout[x][y] == 'L':
            count += 1
            break
    else:
        count += 1

    # SW
    for x, y in zip(range(row+1, len(layout)), range(col-1, 0-1, -1)):
        if layout[x][y] == '#':
            break
        elif layout[x][y] == 'L':
            count += 1
            break
    else:
        count += 1

    # NE
    for x, y in zip(range(row-1, 0-1, -1), range(col+1, len(layout[0]))):
        if layout[x][y] == '#':
            break
        elif layout[x][y] == 'L':
            count += 1
            break
    else:
        count += 1

    # SE
    for x, y in zip(range(row+1, len(layout)), range(col+1, len(layout[0]))):
        if layout[x][y] == '#':
            break
        elif layout[x][y] == 'L':
            count += 1
            break
    else:
        count += 1

    return count


layout = readLayout('seat_layout.txt')

# Part 1
print('\nPart 1!')
prediction = predictOccupancy(layout)
print('Number of seats ending up occupied is:', countOccupiedSeats(prediction))

# Part 2
print('\nPart 2!')
prediction_part2 = predictOccupancy_part2(layout)
print('Number of seats ending up occupied is:', countOccupiedSeats(prediction_part2))

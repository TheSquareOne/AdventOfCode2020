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

                if prev_occupancy[row][col] == 'L' and  adjacent == 0:
                    next_occupancy[row][col] = '#'
                elif prev_occupancy[row][col] == '#' and adjacent >= 4:
                    next_occupancy[row][col] = 'L'


##    for i in next_occupancy:
##        for y in i:
##            print(y, end='')
##        print()

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

layout = readLayout('seat_layout.txt')

##layout = [['.', '.', '.', '#', '#', '#', '.', '.', '.'],
##          ['.', '.', '.', '#', '#', '#', '.', '.', '.'],
##          ['.', '.', '.', '#', '#', '#', '.', '.', '.'],
##          ['.', '.', '.', '#', '#', '#', '.', '.', '.'],
##          ['.', '.', '.', '#', '#', '#', '.', '.', '.'],
##          ['.', '.', '.', '#', '#', '#', '.', '.', '.'],
##          ['.', '.', '.', '#', '#', '#', '.', '.', '.'],
##          ['.', '.', '.', '#', '#', '#', '.', '.', '.'],
##          ['.', '.', '.', '#', '#', '#', '.', '.', '.']]

# Part 1
prediction = predictOccupancy(layout)
print('Number of seats ending up occupied is:', countOccupiedSeats(prediction))

##for i in prediction:
##    for y in i:
##        print(y, end='')
##    print()

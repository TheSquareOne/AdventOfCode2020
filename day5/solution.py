import os

class MySeat:

    def readPasses(self):

        with open(os.path.join(os.path.dirname(__file__), 'boarding_passes.txt'), 'r') as file:
            allPasses = file.readlines()

        return allPasses


    def createSeatMap(self, allPasses):

        rows = 128
        cols = 8
        seatMap = [['O'] * cols for i in range(rows)]

        for boardingPass in allPasses:
            row, col = self.getSeatPosition(boardingPass)
            seatMap[row][col] = 'X'

        return seatMap


    def printSeatMap(self, seatMap):

        row = 0

        for i in seatMap:
            print(row, end=' | ')
            row = row + 1

            for y in i:

                print(y, end=' ')
            print('|')


    def getSeatPosition(self, boardingPass):

        rox = 0
        col = 0
        min_row = 0
        max_row = 127
        min_col = 0
        max_col = 7

        # Row
        for x in range(0, 7):
            if boardingPass[x] == 'F':
                max_row = max_row - (max_row - min_row + 1) / 2
                row = max_row
            elif boardingPass[x] == 'B':
                min_row = min_row + (max_row - min_row + 1) / 2
                row = min_row

        # Col
        for y in range(7, 10):
            if boardingPass[y] == 'L':
                max_col = max_col - (max_col - min_col + 1) / 2
                col = max_col
            elif boardingPass[y] == 'R':
                min_col = min_col + (max_col - min_col + 1) / 2
                col = min_col

        return int(row), int(col)


    def getSeatID(self, row, col):

        return row * 8 + col


    def getHighestSeatID(self, seatMap):

        maxSeatID = 0

        for row in range(len(seatMap)):
            for col in range(len(seatMap[row])):
                if seatMap[row][col] == 'X':
                    seatID = self.getSeatID(row, col)

                    if maxSeatID < seatID:
                        maxSeatID = seatID

        return maxSeatID


    def findMySeat(self, seatMap):

        mySeatID = 0
        seatIDList = []

        # Make list of all occupied seat IDs
        for row in range(len(seatMap)):
            for col in range(len(seatMap[row])):
                if seatMap[row][col] == 'X':
                    seatIDList.append(self.getSeatID(row, col))

        # Check which seat is not accupied and is middle of two occupied seats
        for row in range(len(seatMap)):
            for col in range(len(seatMap[row])):
                
                if seatMap[row][col] == 'O' and \
                    self.getSeatID(row, col - 1) in seatIDList and \
                    self.getSeatID(row, col + 1) in seatIDList:

                    return self.getSeatID(row, col)

        return 'No seat found'


def main():

    app = MySeat()
    allPasses = app.readPasses()

    seatMap = app.createSeatMap(allPasses)
    app.printSeatMap(seatMap)

    print("Highest seat ID occupied currently is:", app.getHighestSeatID(seatMap))
    print("My seat ID is: ", app.findMySeat(seatMap))


if __name__ == '__main__':
    main()

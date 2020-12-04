import os

class Slide:

    map = []

    def readData(self):
        file = open(os.path.join(os.path.dirname(__file__), 'map.txt'), 'r')
        map = file.readlines()
        file.close()

        # Use list instead of string for editing
        for i in range(0, len(map)):
            map[i] = list(map[i][:-1])

        return map


    def countTrees(self, map, x, y):

        count = 0
        x_pos = 0
        mapMultipler = 1

        for i in range(1, len(map)):

            x_pos = x_pos + x

            if len(map[i] * mapMultipler) <= x_pos:
                mapMultipler = mapMultipler + 1

            map[i] = map[i] * mapMultipler

            # Tree
            if map[i][x_pos] == '#':
                count = count + 1
                map[i][x_pos] = 'X'
            # Not tree
            else:
                map[i][x_pos] = 'O'

        # Make each line string instead of list, for prettier print out
        for x in range(0, len(map)):
            map[x] = ''.join(map[x])

        # Print out the map
        for x in map:
            print(x)

        # Write the map on file
        with open(os.path.join(os.path.dirname(__file__), 'route.txt'), 'w') as file:
            for line in map:
                file.write(line + '\n')

        return count

def main():

    app = Slide()
    map = app.readData()
    trees = app.countTrees(map, 3, 1)
    print("There is", trees, "trees on the way!")

if __name__ == "__main__":
    main()

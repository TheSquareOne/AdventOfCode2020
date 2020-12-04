import os

class Slide:

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

        for i in range(0, len(map), y):
            if i == 0:
                continue
                
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
    slope_1_trees = app.countTrees(map, 1, 1)

    map = app.readData()
    slope_2_trees = app.countTrees(map, 3, 1)

    map = app.readData()
    slope_3_trees = app.countTrees(map, 5, 1)

    map = app.readData()
    slope_4_trees = app.countTrees(map, 7, 1)

    map = app.readData()
    slope_5_trees = app.countTrees(map, 1, 2)

    print("There is", slope_1_trees, "trees on the way of 1st slope!")
    print("There is", slope_2_trees, "trees on the way of 2nd slope!")
    print("There is", slope_3_trees, "trees on the way of 3rd slope!")
    print("There is", slope_4_trees, "trees on the way of 4th slope!")
    print("There is", slope_5_trees, "trees on the way of 5th slope!")
    print("In total there is", slope_1_trees + slope_2_trees +
    slope_3_trees + slope_4_trees + slope_5_trees, "trees on the way of slopes!")
    print("And the multiplication of these is", slope_1_trees, "*", slope_2_trees, "*",
            slope_3_trees, "*", slope_4_trees, "*", slope_5_trees, "=",
            (slope_1_trees * slope_2_trees * slope_3_trees * slope_4_trees * slope_5_trees))

if __name__ == "__main__":
    main()

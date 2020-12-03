import os

class Toboggan:

    policies = []
    passwds = []

    def readData(self):

        file = open(os.path.join(os.path.dirname(__file__), 'input.txt'))
        rawData = file.readlines()
        file.close()

        for i in range(0, len(rawData)):
            self.policies.append(rawData[i].split(':')[0])
            self.passwds.append(rawData[i].split(':')[1].lstrip().rstrip('\n'))


    def verifyPasswd(self, part):

        if part == 1:
            count = 0
            for i in range(0, len(self.policies)):
                min, max = self.policies[i].split(' ')[0].split('-')
                char = self.policies[i].split(' ')[1]

                if (self.isPasswdOk(part, int(min), int(max), char, self.passwds[i])):
                    count = count + 1

            return count

        elif part == 2:
            count = 0
            for i in range(0, len(self.policies)):
                pos_1, pos_2 = self.policies[i].split(' ')[0].split('-')
                char = self.policies[i].split(' ')[1]

                if (self.isPasswdOk(part, int(pos_1), int(pos_2), char, self.passwds[i])):
                    count = count + 1

            return count

        else:
            print("There is no such part. Please use part 1 or 2!")


    def isPasswdOk(self, part, min, max, char, passwd):

        if part == 1:
            count = 0
            for c in passwd:
                if c == char:
                    count = count + 1

            if (min <= count) & (max >= count):
                return True
            else:
                return False


        elif part == 2:
            # Be careful; Toboggan Corporate Policies have no concept of "index zero"!
            if ((passwd[min-1] == char) != (passwd[max-1] == char)):
                return True
            else:
                return False


def main():

    app = Toboggan()
    app.readData()

    # Part 1
    okPasswds = app.verifyPasswd(1)
    print("There is", len(app.passwds), "passwords.")
    print("From those", okPasswds, "is OK.")

    # Part 2
    okPasswds = app.verifyPasswd(2)
    print("There is", len(app.passwds), "passwords.")
    print("From those", okPasswds, "is OK.")


if __name__ == "__main__":
    main()

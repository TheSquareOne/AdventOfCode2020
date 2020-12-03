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


    def verifyPasswd(self):

        count = 0
        for i in range(0, len(self.policies)):
            min, max = self.policies[i].split(' ')[0].split('-')
            char = self.policies[i].split(' ')[1]

            if (self.isPasswdOk(int(min), int(max), char, self.passwds[i])):
                count = count + 1

        return count


    def isPasswdOk(self, min, max, char, passwd):

        count = 0
        for c in passwd:
            if c == char:
                count = count + 1

        if (min <= count) & (max >= count):
            return True
        else:
            return False


def main():

    app = Toboggan()
    app.readData()
    okPasswds = app.verifyPasswd()
    print("There is", len(app.passwds), "passwords.")
    print("From those", okPasswds, "is OK.")


if __name__ == "__main__":
    main()

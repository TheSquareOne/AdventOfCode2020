import os

class Scanner:

    def readBatch(self, filename):

        with open(os.path.join(os.path.dirname(__file__), filename), 'r') as file:
            passports = file.readlines()

        return passports


    def countValidPasses(self, passports):

        passportData = ""
        validCount = 0
        for data in passports:

            passportData = passportData + data
            if data == '\n':
                if self.validatePassport(passportData):
                    validCount = validCount + 1
                passportData = ""

        # Check the last one too
        if self.validatePassport(passportData):
            validCount = validCount + 1

        return validCount


    def validatePassport(self, passportData):

        reqField = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
        optField = ['cid']

        for field in reqField:
            if field not in passportData:
                return False
        return True


def main():

    app = Scanner()
    passports = app.readBatch('batch.txt')
    validPasses = app.countValidPasses(passports)
    print("There was", validPasses, "valid passes in the batch.")


if __name__ == "__main__":
    main()

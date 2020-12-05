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

        reqField = {
            'byr':
            {
                'min': 1920,
                'max': 2002
            },
            'iyr':
            {
                'min': 2010,
                'max': 2020
            },
            'eyr':
            {
                'min': 2020,
                'max': 2030
            },
            'hgt':
            {
                'cm': {
                        'min': 150,
                        'max': 193
                      },
                'in': {
                        'min': 59,
                        'max': 76
                      }
            },
            'hcl':
            {
                'prefix': '#',
                'len': 6,
                'min': 0,
                'max': int('f', 16)
            },
            'ecl':
            {
                'color': ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
            },
            'pid':
            {
                'len': 9
            }
        }

        optField = ['cid']


        for field in reqField:
            if field not in passportData:
                return False


        for x in passportData.strip('\n').split('\n'):
            for y in x.split(' '):
                field, value = y.split(':')

                req = reqField.get(field)

                if field == 'hgt':
                    if 'cm' in value:
                        value = value.strip('cm')
                        req = req.get('cm')
                    elif 'in' in value:
                        value = value.strip('in')
                        req = req.get('in')
                    else:
                        return False

                if field == 'byr' or field == 'iyr' or field == 'eyr' or field == 'hgt':
                    if (req['min'] > int(value)) or (int(value) > req['max']):
                        return False

                elif field == 'ecl':
                    if not value in req.get('color'):
                        return False

                elif field == 'pid':
                    if not len(value) == req.get('len'):
                        return False

                elif field == 'hcl':
                    if not value[0] == req.get('prefix') or len(value) == req.get('len'):
                        return False

                    for c in value[1::]:
                        if (int(c, 16) < 0) or (int(c, 16) > 15):
                            return False

                elif field in optField:
                    # Optional -> no validation
                    pass

                else:
                    # This should never happen
                    print("Invalid field", field, "encountered!")
                    return False

        return True


def main():

    app = Scanner()
    passports = app.readBatch('batch.txt')
    validPasses = app.countValidPasses(passports)
    print("There was", validPasses, "valid passes in the batch.")

#    min_test = "byr:1920 iyr:2010 eyr:2020 hgt:150cm hcl:#123456 ecl:amb pid:000000000"
#    print(app.validatePassport(min_test))

if __name__ == "__main__":
    main()

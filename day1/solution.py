import os

class Expense:

    def readData(self):

        report_file = open(os.path.join(os.path.dirname(__file__),"expense_report.txt"), "r")
        self.expense_report = report_file.readlines()
        report_file.close()

        for i in range(0, len(self.expense_report)):
            self.expense_report[i] = int(self.expense_report[i].rstrip('\n'))

        return self.expense_report


    def findEntries(self, entries = 2, sum = 2020):

        if entries == 2:
            for i in range(0, len(self.expense_report) - 1):
                for y in range(i + 1, len(self.expense_report)):
                    if (self.expense_report[i] + self.expense_report[y]) == sum:
                        return self.expense_report[i], self.expense_report[y]

        elif entries == 3:
            for i in range(0, len(self.expense_report) - 2):
                for y in range(i + 1, len(self.expense_report) - 1):
                    for z in range(y + 1, len(self.expense_report)):
                        if (self.expense_report[i] + self.expense_report[y] + self.expense_report[z]) == sum:
                            return self.expense_report[i], self.expense_report[y], self.expense_report[z]

        else:
            print("Please use amount of entries 2 or 3!")

        print("No matching entries found!")
        return 0


def main():

    app = Expense()
    app.readData()
    entry_1, entry_2 = app.findEntries()
    print(entry_1, " + ", entry_2, " = ", entry_1 + entry_2)
    print(entry_1, " * ", entry_2, " = ", entry_1 * entry_2)

    entry_1, entry_2, entry_3 = app.findEntries(3, 2020)
    print(entry_1, " + ", entry_2, " + ", entry_3, " = ", entry_1 + entry_2 + entry_3)
    print(entry_1, " * ", entry_2, " * ", entry_3, " = ", entry_1 * entry_2 * entry_3)

if __name__ == "__main__":
    main()

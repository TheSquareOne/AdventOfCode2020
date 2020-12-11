import os

class GroupsAnswers:

    def readAnswers(self, filename):

        with open(os.path.join(os.path.dirname(__file__), filename), 'r') as file:
            answers = file.readlines()

        return answers


    def countYes(self, answers):

        sum = 0
        answerList = ""

        for x in answers:
            count = 0
            answerList = answerList + x

            if x == '\n':
                for i in range(ord('a'), ord('z') + 1):
                    if chr(i) in answerList:
                        count = count + 1
                sum = sum + count
                answerList = ""
        else:
            for i in range(ord('a'), ord('z') + 1):
                if chr(i) in answerList:
                    count = count + 1
            sum = sum + count
            answerList = ""

        return sum


def main():

    app = GroupsAnswers()
    answers = app.readAnswers('group_answers.txt')
    print("Groups answered 'yes' a total of", app.countYes(answers), "times.")


if __name__ == "__main__":
    main()

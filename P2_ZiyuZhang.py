class MinusError(Exception):
    def __init__(self, Msg):
        super().__init__(self)
        self.Msg = Msg

    def __str__(self):
        return self.Msg
# Define a user error in order to check if minus is entered.


class RangeError(Exception):
    def __init__(self, Msg):
        super().__init__(self)
        self.Msg = Msg

    def __str__(self):
        return self.Msg
# Define a user error in order to check if input is out of range.


def MinusCheck(value):
    if value < 0:
        msg = 'Found negative value: ' + str(value) + '\n'
        raise MinusError(msg)
    else:
        return value
# Define a fuction to raise MinusError.


def RangeCheck(value):
    if 0 <= value <= 100:
        return value
    else:
        msg = str(value) + 'is out of range. \n'
        raise RangeError(msg)
# Define a function to raise RangeError.


def InputScore():
    score = input('Please input your score, input Q/q to quit: ')
    return score
# 

def CheckInput(string):
    try:
        score = float(string)
        MinusCheck(score)
        RangeCheck(score)
    except ValueError:
        print('Please input a numerical format of your scores. \n')
    except MinusError:
        print('You just input a nagative score. \n')
    except RangeError:
        print('The score you entered is not between 0 and 100. \n')
    else:
        return score


def Classify(score):
    if score < 70:
        return 'F'
    elif 70 <= score < 80:
        return 'C'
    elif 80 <= score < 83:
        return 'B-'
    elif 83 <= score < 87:
        return 'B'
    elif 87 <= score < 90:
        return 'B+'
    elif 90 < score <= 93:
        return 'A-'
    else:
        return 'A'


def main():
    status = True
    while status:
        score = InputScore()
        if 'Q' == score or 'q' == score:
            status = False
            print('Thank you for using. \n')
            break
        FloatScore = CheckInput(score)
        Rank = Classify(FloatScore)
        print('Your rank is ', Rank, '\n')

    print('End. \n')


if __name__ == '__main__':
    main()

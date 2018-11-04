# @author:Ziyu Zhang


def get_line(path):
    try:
        fp = open(path, 'r')
    except FileNotFoundError:
        print('Cannot open ', path, ' , plz check. ')
    else:
        with fp:
            for line in fp:
                string = 'X-DSPAM-Confidence:'
                if line.find(string) >= 0:
                    number = line[len(string):]
                    # I made this function a generator. So it will return something we I need
                    yield number


def check_number(number):
    # If it is not a float number, return None.
    try:
        FloatNum = float(number)
    except ValueError:
        return None
    else:
        return FloatNum


def get_file_name():
    name = input('Input your file name: ')
    return name


def get_mean(List):
    if len(List) == 0:
        # This is important
        raise ZeroDivisionError('Maybe you input a empty file, or there is no float number in spam confidence. ')
    Sum = 0
    for i in List:
        Sum += i
    return Sum / len(List)


def main():
    while True:
        quit = input('Input q/Q to quit, any other to continue: ')
        if quit.lower() == 'q':
            break
        try:
            name = get_file_name()
            NumList = []
            LineGen = get_line(name)
            for item in LineGen:
                FloatNum = check_number(item)
                if FloatNum is not None:
                    # To make sure I will get a float number
                    NumList.append(FloatNum)

            mean = get_mean(NumList)
            print('Average spam confidence: {:.4f}'.format(mean))
        except ZeroDivisionError as z:
            print(z)


if __name__ == '__main__':
    main()

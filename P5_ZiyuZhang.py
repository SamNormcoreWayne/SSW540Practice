# @Author: Ziyu Zhang


def SplitStrings(string):
    # Split string into words as list
    Splited = string.split()
    return Splited


def CombineStrings(Splited):
    # Combine words into a list
    Combined = " ".join(Splited)
    return Combined


def SingleToPlural(string):
    # Main part of this program
    for i in string:
        # Check input whether it is a word or not.
        if not i.isalpha():
            raise ValueError('You did not input a word. ')

    if(string.endswith('y')):
        if string[-1:-2] in 'aeiou':
            return string + 's'
        else:
            return string[:-1] + 'ies'

    if string[-1:] in 'osxz':
        return string + 'es'
    elif string[-2:] in ['ch', 'sh']:
        return string + 'es'

    return string + 's'


def main():
    # main function
    string = input('Input some words: ')
    Splited = SplitStrings(string)

    try:
        for i in range(len(Splited)):
            Splited[i] = SingleToPlural(Splited[i])
    except ValueError as e:
        print(e)

    string = CombineStrings(Splited)
    print(string)


if __name__ == '__main__':
    main()

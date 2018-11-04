# @author: Ziyu Zhang
# This program is for gussing numbers.
import random


def randomNum():
    return random.randint(1, 20)
# Do not ask me why this function only has 1 line. I like modification.


def State(num, ran):
    # A functiun with 2 parameters.
        if ran < int(num):
            return 1
        elif ran > int(num):
            return -1
        else:
            return 0


def GuessNum():
    # This is the main part of my code.
    ran = randomNum()
    name = input("What is your name? ")
    print("I am thinkin a number between 1 and 20. \n")
    for i in range(0, 6):
        num = input('Take a guess: ')
        if not num.isdigit():
            raise ValueError('You did not input a right number. \n')
        elif int(num) < 1 or int(num) > 20:
            raise ValueError('The number input is not between 1 and 20. \n')
        StateDic = {1: 'Your guess is too high. \n', -1: 'Your guess is too low'}
        state = State(num, ran)
        if state == 0:
            print("Good Job" + name + '\n')
            break
        else:
            print(StateDic[state])
    print('The number is ' + str(ran) + '. \n')


def main():
    # main part.
    while True:
        quit = input('input "quit" to quit, enter any other to continue. ')
        if quit == 'quit':
            break
            # if wanna quit, just break.
        else:
            try:
                GuessNum()
            except ValueError as v:
                print(v)


if __name__ == '__main__':
    main()

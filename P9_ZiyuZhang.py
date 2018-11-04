# @author: Ziyu Zhang
# SSW 540 P9 Classic Books

from string import punctuation
from collections import defaultdict
import os


def get_line(path):
    try:
        fp = open(path, 'r')
    except FileNotFoundError:
        print('Cannot open ', path, ', plz check. ')
    else:
        with fp:
            for line in fp:
                if line.strip(' \n\r') == '':
                    continue
                yield line.strip(' \n\r')


class ClassicBook:
    """
    I designed this Homework as a class.
    Because I found if I use process-oriented programming, \
    all functions would use one same parameter which is the dictionary of all words.
    And it is easier to create many instances like txt for testing or else.
    """

    def __init__(self):
        self.words_dic = defaultdict(int)
        self.path = str()
        self.words = list()

    def get_path(self, file_name='test.txt', path=os.getcwd()):
        # Be careful when you input the dir of flie.
        self.path = os.path.join(path, file_name)

    def get_words_dic(self):
        lines = get_line(self.path)
        for line in lines:
            translator = str.maketrans({key: ' ' for key in punctuation})
            string = line.translate(translator)
            for word in string.split(' '):
                word = word.strip()
                if word == '':
                    # delete empty characters.
                    continue
                if word.isalpha():
                    self.words_dic[word.lower()] += 1

        return self.words_dic.items()

    def get_words_num(self):
        num = 0
        for count in self.words_dic.values():
            num += count
        return '{:,}'.format(num)

    def get_distinct_words(self):
        words_tp = tuple(self.words_dic.keys())
        return '{:,}'.format(len(words_tp))

    def get_top_25(self):
        self.words = sorted(self.words_dic.items(), key=lambda x: x[1], reverse=True)
        return self.words[:25]

    def get_sorted(self):
        if len(self.words) > 0:
            return sorted(self.words)


def main():
    tom_sawyer = ClassicBook()
    tom_sawyer.get_path(file_name='TomSawyer.txt', path='C://Users//64937//OneDrive//Documents//SSW//540//')
    # You can change the path to your directory here.
    tom_sawyer.get_words_dic()
    print(tom_sawyer.get_words_num())
    print(tom_sawyer.get_distinct_words())
    print(tom_sawyer.get_top_25())
    print(tom_sawyer.get_sorted())


if __name__ == '__main__':
    main()

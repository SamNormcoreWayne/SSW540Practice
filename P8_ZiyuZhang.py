# @author: ZiyuZhang
# SSW540 P8: Counting unique items

from collections import defaultdict


class MailValueError(Exception):
    def __init__(self, Msg='Wrong format of mails.'):
        super().__init__(self)
        self.Msg = Msg

    def __str__(self):
        return self.Msg


def get_line(path):
    try:
        fp = open(path, 'r')
    except FileNotFoundError:
        print('Cannot open ', path, ' , plz check. ')
    else:
        with fp:
            for line in fp:
                string = 'From:'
                if line.find(string) >= 0:
                    email = line[len(string):].strip()
                    # I made this function a generator. So it will return something we I need
                    yield email


def check_mail(mail):
    # Just simply check the format of emails.
    # So every email should contain '@' and '.' at least, or I would raise MailValueError
    check = [True, True]
    for item in mail:
        if item == '@':
            check[0] = False
        if item == '.':
            check[1] = False
    if not any(check):
        return True
    else:
        raise MailValueError()


def mail_counter(path):
    email_dict = defaultdict(int)
    for mail in get_line(path):
        try:
            check_mail(mail)
        except MailValueError as m:
            print(m)
        else:
            email_dict[mail] += 1
    # Sort dictiomnary by its values
    return sorted(email_dict.items(), key=lambda x: x[1], reverse=True)[0]


def main():
    path = 'mbox.txt'
    counter = mail_counter(path)
    print('Mail: {} Numbers: {}'.format(counter[0], counter[1]))


if __name__ == '__main__':
    main()

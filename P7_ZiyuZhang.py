# @Author: ZiyuZhang
# P7 for SSW 540


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


def save_and_count(path):
    mail_set = set()
    for mail in get_line(path):
        mail_set.add(mail)
    for mail in mail_set:
        try:
            check_mail(mail)
        except MailValueError as m:
            print(m)
    return list(mail_set), len(mail_set)


def main():
    path = 'mbox.txt'
    mails, numbers = save_and_count(path)
    print('The numbers of mails in mbox.txt: {}'.format(numbers))

    path = 'mbox-short.txt'
    mails, numbers = save_and_count(path)
    print('The numbers of mails in mbox-short.txt: {}'.format(numbers))


if __name__ == '__main__':
    main()

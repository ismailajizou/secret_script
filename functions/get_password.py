from Account.account import account
from bcrypt import checkpw
from getpass import getpass
from functions.apparance import spacing, interface, pause
from .open_folder import open_folder


def is_true_password(input_pwd: str):
    hashed_pwd = account.hashed_pwd
    password = input_pwd.encode()
    return checkpw(password, hashed_pwd)


def get_pwd():
    input_password = getpass()
    counter = 2
    if is_true_password(input_password):
        open_folder()
    else:
        while counter > 0:
            interface()
            print(f'WRONG PASSWORD: {counter} attempts left ! \n')
            input_password = getpass()
            if is_true_password(input_password):
                open_folder()
                break
            else:
                counter -= 1
        else:
            spacing()
            print('\t\tAm I a joke for you  -_-')
            pause()


if __name__ == '__main__':
    get_pwd()

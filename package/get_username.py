from Account.account import account
from package.get_password import get_pwd
from package.apparance import spacing, interface, pause


def is_username_true(input_username: str):
    return account.username == input_username


def check_username():
    try:
        input_username = input('Username: ')
        if is_username_true(input_username):
            interface()
            print(
                f'\n Hello {account.username}, please enter the password to access your secret folder !\n')
            print('\t\tPassword will be hidden for security reasons\n\n')
            get_pwd()
        else:
            spacing()
            print('INVALID USERNAME !')
            pause()
    except KeyboardInterrupt:
        exit()

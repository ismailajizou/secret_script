from functions.apparance import spacing, interface, pause
from functions.get_password import get_pwd
from Account.account import account
import os


def main():
    os.system('color a')
    try:
        interface()
        username = account.username
        input_username = input('Username: ')
        if input_username == username:
            interface()
            print(f'\n Hello {username}, please enter the password to access your secret folder !\n')
            print('              Password will be hidden for security reasons\n\n')
            get_pwd()
        else:
            spacing()
            print('INVALID USERNAME !')
            pause()
    except KeyboardInterrupt:
        exit()


if __name__ == '__main__':
    main()

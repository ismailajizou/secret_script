from os import path, startfile
from package.apparance import spacing, pause
from Account.account import account


def open_folder():
    try:
        username = account.username
        spacing()
        print(f'                           HELLO {username} ! ')
        print('                  WELCOME TO YOUR SECRET FOLDER !')
        startfile(path.dirname(account.secret_folder_path))
        pause()
    except:
        print('Could not find the folder : incorrect path')

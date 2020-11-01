import os
from functions.apparance import spacing, pause
from Account.account import account

def open_folder():
    try:
        username = account.username
        spacing()
        print(f'                           HELLO {username} ! ')
        print('                  WELCOME TO YOUR SECRET FOLDER !')
        os.startfile(os.path.dirname(account.secret_folder_path))
        pause()
        os.remove('../null.txt')
    except:
        print('Could not find the folder : incorrect path')

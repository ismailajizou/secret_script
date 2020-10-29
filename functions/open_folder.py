import os
from functions.apparance import spacing, pause
from Account.account import account

def open_folder():
    username = account.username
    spacing()
    print(f'                           HELLO {username} ! ')
    print('                  WELCOME TO YOUR SECRET FOLDER !')
    os.startfile(os.path.dirname(account.secretfolder_path))
    pause()

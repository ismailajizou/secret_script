from getpass import getpass
import bcrypt
import os

def pause():
    os.system('pause >> null.txt')


def spacing():
    os.system('cls')
    for i in range(1, 10):
        print()

def greeting():
    os.system('cls')
    print('''
    ######################################################

    #  ███████╗███████╗ ██████╗██████╗ ███████╗████████╗ #  
    #  ██╔════╝██╔════╝██╔════╝██╔══██╗██╔════╝╚══██╔══╝ #   
    #  ███████╗█████╗  ██║     ██████╔╝█████╗     ██║    # 
    #  ╚════██║██╔══╝  ██║     ██╔══██╗██╔══╝     ██║    #   
    #  ███████║███████╗╚██████╗██║  ██║███████╗   ██║    #  
    #  ╚══════╝╚══════╝ ╚═════╝╚═╝  ╚═╝╚══════╝   ╚═╝    #   

    ######################################################
    ''')


# In the function below you must past the full path to your hidden folder
def open_folder():
    spacing()
    print('                           HELLO USER! ')
    print('                  WELCOME TO YOUR SECRET FOLDER !')
    os.system('start ..')
    pause()


def get_password():
    p = getpass()
    return p.encode()


greeting()

# you must past your hashed password in the 'hashed_pwd' variable

hashed_pwd = b'hashed password'

counter = 2
username = input('Username: ')

if username == 'username':
    greeting()
    print(f'\n Hello {username}, please enter the password to access your secret folder !\n')
    print('              Password will be hidden for security reasons\n')
    password = get_password()
    if bcrypt.checkpw(password, hashed_pwd):
        open_folder()

    else:
        while counter > 0:
            greeting()
            print(f'Wrong password: {counter} attempts left ! \n')
            password = get_password()

            if bcrypt.checkpw(password, hashed_pwd):
                open_folder()
                break

            else:
                counter -= 1

        else:
            spacing()
            print('INVALID USERNAME !')
            pause()

else:
    spacing()
    print('INVALID USERNAME !')
    os.system(f'echo {username}>> null.txt')
    pause()

from getpass import getpass
import bcrypt
import os

os.system('color a')


def pause():
    os.system('pause >> null.txt')


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
    os.system('cls')
    for i in range(1, 10):
        print()

    print('                           HELLO Ismail ! ')
    print('                  WELCOME TO YOUR SECRET FOLDER !')
    os.system('start C:\\Users\\dell\\Desktop\\Secretfolder')
    pause()


def get_password():
    p = getpass()
    return p.encode()


greeting()

# you must past your hashed password in the 'hashed_pwd' variable

hashed_pwd = b'$2b$12$/rmTLlUMpdqWqzogvi1np.wiVuNVgOL.Eqp1AEgYvKMhtLYIit942'

counter = 2
username = input('Username: ')

if username == 'Ismail Aj':
    greeting()
    print(f'\n Hello Ismail, please enter the password to access your secret folder !\n')
    print('              Password will be hidden for security reasons                  ')
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
            print('                 Am I a joke for you  -_-')
            pause()

else:
    print('INVALID USERNAME !')
    os.system(f'echo {username}>> null.txt')
    pause()

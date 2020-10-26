from getpass import getpass
import bcrypt
import os


def pause():
    os.system('pause >> null.txt')


def spacing():
    os.system('cls')
    for i in range(1, 10):
        print()


def interface():
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


def open_folder():
    spacing()
    print('                           HELLO username ! ')
    print('                  WELCOME TO YOUR SECRET FOLDER !')
    os.startfile(os.path.dirname(os.getcwd()))
    pause()


def is_true_password(input_pwd: str):
    hashed_pwd = b'hashed password'
    password = input_pwd.encode()
    return bcrypt.checkpw(password, hashed_pwd)


def get_pwd():
    input_password = getpass()
    counter= 2
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
            print('                 Am I a joke for you  -_-')
            pause()


def main():
    interface()
    username = input('Username: ')
    if username == 'username':
        interface()
        print(f'\n Hello {username}, please enter the password to access your secret folder !\n')
        print('              Password will be hidden for security reasons\n\n')
        get_pwd()
    else:
        spacing()
        print('INVALID USERNAME !')
        os.system(f'echo {username}>> null.txt')
        pause()


if __name__ == '__main__':
    main()
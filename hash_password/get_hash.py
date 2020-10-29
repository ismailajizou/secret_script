import bcrypt
import os

def main():
    p = input('Type the password you want to hash: ')
    password = p.encode()
    salt = bcrypt.gensalt()
    print('result: ', end='')
    print(bcrypt.hashpw(password, salt))
    os.system('pause >> null.txt')


if __name__ == '__main__':
    main()
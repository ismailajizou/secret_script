import bcrypt
import os
# Running this program you will  get the hash of your input password


p = input('Type the password you want to hash: ')
password = p.encode()
salt = bcrypt.gensalt()
print('result: ', end='')
print(bcrypt.hashpw(password, salt))
os.system('pause >> null.txt')

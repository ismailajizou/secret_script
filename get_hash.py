import bcrypt

# Running this program you will  get the hash of your input password


p = input()
password = p.encode()
salt = bcrypt.gensalt()

print(bcrypt.hashpw(password, salt))

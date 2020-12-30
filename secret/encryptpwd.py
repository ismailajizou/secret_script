from bcrypt import hashpw, gensalt


def encryptPass(password: str):
    return hashpw(password.encode(), gensalt())


if __name__ == '__main__':
    encryptPass()

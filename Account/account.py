from os import getcwd, path
from secret.encryptpwd import encryptPass


def create_user_account():
    default = "user"
    if not path.exists("Account/username.txt"):
        with open("Account/username.txt", "w") as f:
            f.write(default)
            f.close()
    if not path.exists("Account/password.txt"):
        with open("Account/password.txt", "wb") as f:
            f.write(encryptPass(default))
            f.close()


def reading_acc(field: str):
    try:
        create_user_account()
        with open(f"Account/{field}.txt", "r") as f:
            coord = f.readlines()
            f.close()
        return coord[0]
    except:
        exit()


class Account:
    def __init__(self):
        self.username = reading_acc("username")
        self.hashed_pwd = reading_acc("password").encode()
        self.secret_folder_path = getcwd()

account = Account()

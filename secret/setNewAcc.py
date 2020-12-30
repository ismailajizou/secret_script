from getpass import getpass
from package.get_username import is_username_true
from package.get_password import is_true_password
from package.apparance import interface, pause
from Account.account import account
from secret.encryptpwd import encryptPass


def changePwdAndUsername(username: str, pwd: str):
    try:
        with open("Account/username.txt", "w") as f:
            f.write(username)
            f.close()
        with open("Account/password.txt", "wb") as f:
            f.write(encryptPass(pwd))
            f.close()
    except Exception as err:
        print("Oooops!!",err.__class__, "occured!")
        pause()


def setNewAcc():
    try:
        interface()
        username = input("Enter your old username: ")
        pwd = getpass()
        if not is_username_true(username):
            print("Wrong username!")
            pause()
        elif not is_true_password(pwd):
            print("Wrong password!")
            pause()
        elif(is_username_true(username) and is_true_password(pwd)):
            interface()
            print("\n\n-----------Change Account------------")
            print("\tbelow you'll be asked for a new username and password.")
            print("\tLeaving the username field blank means keeping the old value.")
            print("\tPassword must be at least 6 characters long.\n")
            newName = input(f"New username ({account.username}): ")
            newPass = input("New Password: ")
            confirmPass = input("Confirm Password: ")
            if(newPass == confirmPass and len(newPass) >= 6):
                if(newName):
                    changePwdAndUsername(newName, newPass)
                else:
                    changePwdAndUsername(account.username, newPass)
                print("Account changed successfully")
                pause()
            else:
                print("Something went wrong try again later!")
                pause()
    except:
        exit()


if __name__ == '__main__':
    setNewAcc()

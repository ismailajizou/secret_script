from package.apparance import interface, pause
from secret.secret import secret
from secret.setNewAcc import setNewAcc


def main():
    try:
        interface()
        print("Hello To your secret script")
        print("\t1-Open your Secret Folder")
        print("\t2-Set new Username & Password\n")

        choice = int(input("Your choice: "))

        if (choice == 1):
            secret()
        elif(choice == 2):
            setNewAcc()
        else:
            print("UNVALID CHOICE !!")
            pause()
    except:
        exit()


if __name__ == "__main__":
    main()

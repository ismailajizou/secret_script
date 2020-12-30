from package.get_username import check_username
from package.apparance import interface


def secret():
    try:
        interface()
        check_username()
    except:
        exit()


if __name__ == '__main__':
    secret()

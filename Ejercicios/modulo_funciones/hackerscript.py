import os

FILE="eps3.7dont-delete-me.ko"


def main():
    desktop_path = "/home/" + os.getlogin() + "/Desktop/"
    a = open(desktop_path + FILE, "w")
    a.write("Don't delete me ")
    a.close()


if __name__ == "__main__":
    main()

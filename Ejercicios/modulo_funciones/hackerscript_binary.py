import os

desktop_path = "/home/" + os.getlogin() + "/Desktop/"
FILE = desktop_path + "eps3.7dont-delete-me.ko"


def main():
    with open(FILE, 'wb') as a:
        a.write(os.urandom(1024))  # replace 1024 with size_kb if not unreasonably large


if __name__ == "__main__":
    main()

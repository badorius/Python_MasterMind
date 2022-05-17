#https://stackoverflow.com/questions/43557929/conversion-of-string-to-upper-case-without-inbuilt-methods
def mayus_conv(palabra):
    for letter in palabra:
        s = ord(letter)
        if 97 <= s <= 122:
            print(chr(s - 32), end="")


def main():
    palabra=input("Introducir una palabra en minúsculas: ")
    mayus_conv(palabra)


if __name__ == "__main__":
    main()
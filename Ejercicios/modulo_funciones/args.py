from time import sleep

def medir_largos(iterable, *args):
    if args:
        largos=[len(iterable)]
        for a in args:
            largos.append(len(a))
        return largos
    return len(iterable)


def main():
    print(medir_largos("hola"))
    print(medir_largos("hola", "como", "estas"))

if __name__ == "__main__":
    main()

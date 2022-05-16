def medir_largos(iterable, *args):
    largos = [iterable]
    if args:
        largos = [iterable]
        for a in args:
            largos.append(a)
        return max(largos, key=len)
    return max(largos, key=len)


def main():
    print(medir_largos("hola", "como", "estas"))


if __name__ == "__main__":
    main()
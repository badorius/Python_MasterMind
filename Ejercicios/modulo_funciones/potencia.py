from time import sleep

def potencia(num, elevado=2):
    total = 1
    for i in range(elevado):
        print("{} * ".format(num),end="")
        total = total * num

    return total


def main():
    print(" = ", potencia(2, elevado=4))

if __name__ == "__main__":
    main()

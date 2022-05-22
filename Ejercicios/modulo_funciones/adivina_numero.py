import random
random_number = random.randint(1,100)

def check_minor_major(usernumber, pcnumber):
    if usernumber < pcnumber:
        print("El numero introducido es inferior, intente de nuevo.")
    elif usernumber > pcnumber:
        print("El numero introducideo es superior, intente de nuevo")

def adivina(pcnumber):
    usernumber = input("Adivina un número del 1 al 100: ")

    while usernumber != pcnumber or not usernumber.isnumeric():
        usernumber=input("Adivina un número del 1 al 100: ")
        if usernumber.isnumeric():
            check_minor_major(int(usernumber), int(pcnumber))

    print(" {} = {} Has acertado!!!".format(usernumber, pcnumber))


def main():
    adivina(random_number)

if __name__ == "__main__":
    main()

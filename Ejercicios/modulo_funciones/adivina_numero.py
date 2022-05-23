import random
random_number = random.randint(1,100)

# Input function force user to enter a digit
def _input():
    usernumber = "Wrong"
    while usernumber.isdigit() == False:
        usernumber = input("Adivina un número del 1 al 100: ")

        if usernumber.isdigit() == False:
            print("Error! Adivina un número del 1 al 100: ")
        else:
            return int(usernumber)

# Function check if user number is major or minor to give a hint to user
def check_minor_major(usernumber, pcnumber):
    if usernumber < pcnumber:
        print("El numero introducido es inferior, intente de nuevo.")
    elif usernumber > pcnumber:
        print("El numero introducideo es superior, intente de nuevo")


# Function ask user a number until It is equal that random number.
def adivina(pcnumber):
    usernumber = None

    while usernumber != pcnumber:
        usernumber = _input()
        check_minor_major(usernumber, pcnumber)

    print(" {} = {} Has acertado!!!".format(usernumber, pcnumber))


def main():
    adivina(random_number)

if __name__ == "__main__":
    main()

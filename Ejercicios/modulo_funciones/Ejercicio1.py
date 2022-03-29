from daemons_names import daemons

def main(number):
    return daemons[number]

if __name__ == "__main__":
    while True:
        user_numero = 0
        while user_numero not in range(1, 31):
            user_numero = int(input("Introduce el día del més en que naciste (1-31): "))

        daemon_text = main(user_numero)
        print("Naciste en el día de -> {}".format(daemon_text))


from time import sleep

def c():
    print("c")
    sleep(1)
    a()

def b():
    print("b")
    sleep(1)
    c()

def a():
    print("a")
    sleep(1)
    b()

def main():
    a()

if __name__ == "__main__":
    main()

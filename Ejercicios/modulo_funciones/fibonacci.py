from time import sleep
MAX_NUM = 30000000

def sumar_uno(a, b):
    next_num = a + b
    print("{}, ".format(next_num),end ="")
    a = b
    b = next_num
    if next_num<= MAX_NUM:
        sumar_uno(a, b)

def main():
    a = 0
    b = 1
    sumar_uno(a, b)

if __name__ == "__main__":
    main()

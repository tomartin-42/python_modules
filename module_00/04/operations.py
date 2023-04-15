import sys

def sum(num1, num2):
    print("Sum: " + "\t" + "\t", int(num1 + num2))

def res(num1, num2):
    print("Diference: " + "\t", int(num1 - num2))

def product(num1, num2):
    print("product: " + "\t", int(num1 * num2))

def quo(num1, num2):
    res = ""
    try:
        num1 / num2
    except:
        res = 'ERROR (div by zero)'
    else:
        res = str(num1 / num2)
    finally:
        print("Quotient: " + "\t" + res)

def mod(num1, num2):
    res = ""
    try:
        num1 / num2
    except:
        res = 'ERROR (modulo by zero)'
    else:
        res = str(int(num1 % num2))
    finally:
        print("Remainder: " + "\t" + res)

def other():
    usage = 'Usage: python operations.py <number1> <number2>\nExample:\n\tpython operations.py 10 3'

    try:
        num1 = int(sys.argv[1])
        num2 = int(sys.argv[2])
    except ValueError:
        print("AssertionError: only integers")
        exit()

    if len(sys.argv) == 1:
        print(usage)
        exit()
    if len(sys.argv) > 3:
        print("AssertionError: too many arguments")
        exit()

    print(num1, num2)
    sum(num1, num2)
    res(num1, num2)
    product(num1, num2)
    quo(num1, num2)
    mod(num1, num2)

if __name__ == '__main__':
    other()
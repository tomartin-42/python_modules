import sys
import argparse

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
    if len(sys.argv) > 3:
        raise AssertionError("too many arguments")
    parser = argparse.ArgumentParser(usage='%(prog)s <number1> <number2>\nExample:\n\tpython operations.py 10 3' )
    parser.add_argument('number1', type = int)
    parser.add_argument('number2', type = int)
    args = parser.parse_args()
    # con vars(args) se imprime los argumentos que contiene args
    print(vars(args))
    sum(args.number1, args.number2)
    res(args.number1, args.number2)
    product(args.number1, args.number2)
    quo(args.number1, args.number2)
    mod(args.number1, args.number2)

if __name__ == '__main__':
    try:
        other()
    except AssertionError as err:
        print('AssertionError:', err)
        exit(1)
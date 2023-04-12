import sys
import argparse
# buena explicacion de excepciones en 
# https://www.w3schools.com/python/python_try_except.asp

<<<<<<< HEAD
def suma(num1, num2):
    print("Sum: ", num1 + num2)
=======
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
>>>>>>> 5f41b0fbc0913731bc7062f0863b287d29110c51

def mod(num1, num2):
    res = ""
    try:
        num1 / num2
    except:
        res = 'ERROR (modulo by zero)'
    else:
        res = str(int(num1 / num2))
    finally:
        print("Remainder: " + "\t" + res)
def other():
<<<<<<< HEAD
    parser = argparse.ArgumentParser(usage="python operations.py <number1> <number2>")
    parser.add_argument('<number1>', type = int)
    parser.add_argument('<number2>', type = int)
    args = parser.parse_args()
   # suma(args.<number1>, args.<number2>)
=======
    parser = argparse.ArgumentParser()
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
>>>>>>> 5f41b0fbc0913731bc7062f0863b287d29110c51

if __name__ == '__main__':
    other()

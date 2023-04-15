import sys
import string
import signal

def headler(signum, frame):
    if signum == signal.SIGINT:
        print("KeyboardInterrupt")
        exit(0)

def text_analyzer(*text_a):
    """
    This function counts the number of upper characters, lower characters,
    punctuation and spaces in a given text
    """
    text = list(text_a)

    signal.signal(signal.SIGINT, headler)

    try:
        if len(text) == 0:
            print("What is the text to analyze?")
            text.append(input())
    except EOFError:
        text.append("")

    if not isinstance(text[0], str):
        print("Asertion error: the input is not a string")
        return
    
    if len(text) > 2:
        print("Error: only one argument is allowed")
        exit()
    
    U = L = S = C = T = 0

    for i in text[0]:
        if i.isupper():
            U += 1
        if i.islower():
            L += 1
        if i in string.punctuation:
            C += 1
        if i == ' ':
            S += 1
        T += 1

    print(f"The text contains {T} character(s):")
    print(f"- {U} Upper")
    print(f"- {L} Lower")
    print(f"- {C} Puntuation")
    print(f"- {S} Spaces")

if __name__ == '__main__':

    text_analyzer(sys.argv[1])
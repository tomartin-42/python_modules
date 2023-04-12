import sys
import string

def text_analizer(*text):
    """
    This function counts the number of upper characters, lower characters,
    punctuation and spaces in a given text
    """

    if len(text) == 0 or text[0] == None:
        print("What is the text to analyze?")
        return

    if not isinstance(text[0], str):
        print("Asertion error: the input is not a string")
        return
    
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
    if len(sys.argv) > 2:
        print("Error: only one argument is allowed")
        exit()

    if len(sys.argv) == 1:    
        print("What is the text to analyze?")
        exit()

    text_analizer(sys.argv[1])
import sys
import string

def count_analizer(text):

    U = 0
    L = 0
    S = 0
    C = 0

    for i in text:
        if i.isupper():
            U += 1
        if i.islower():
            L += 1
        if i in string.punctuation:
            C += 1
        if i == ' ':
            S += 1

    print("Upper= ", U)
    print("Lower= ", L)
    print("Spaces= ", S)
    print("Special= ", C)

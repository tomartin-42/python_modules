import morse
import sys

answer = []

for a in sys.argv[1:]:
    for l in a:
        if not l.upper() in morse.MORSE:
            print("ERROR")
            exit(1)
res = ""
for a in sys.argv[1:]:
    for l in a:
        res += morse.MORSE[l.upper()] + ' '
    res += "/ " 
print(res[:-2])

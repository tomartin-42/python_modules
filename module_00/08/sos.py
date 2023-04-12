import morse
import sys
answer = []
data = sys.argv[1]
for l in data:
    if not l.upper() in morse.MORSE:
        print("ERROR.")
        exit(1)
for l in data:
    print(morse.MORSE[l.upper()], end=' ')
print()

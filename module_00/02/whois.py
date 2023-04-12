import sys

if int(sys.argv[1]) == 0:
    print("Zero")
    sys.exit()

print(('Even', 'Odd')[int(sys.argv[1])%2])

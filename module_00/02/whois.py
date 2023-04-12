import sys

if len(sys.argv) < 2:
    print()
    sys.exit()

if len(sys.argv) > 2:
    print("AssertionError: more than one argument are provided")
    sys.exit()

if not sys.argv[1].isdigit():
    print("AssertionError: argument is not an integer")
    sys.exit()

if int(sys.argv[1]) == 0:
    print("Zero")
    sys.exit()

print(('Even', 'Odd')[int(sys.argv[1]) % 2])

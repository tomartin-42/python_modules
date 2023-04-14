import sys
import argparse
import string

if len(sys.argv) != 3: # 1
    print('ERROR')
    exit() 
if sys.argv[1] is None or sys.argv[2] is None:
    print('ERROR')
    exit()
if not isinstance(sys.argv[1], str):
    print('ERROR')
    exit()
if not sys.argv[2].isdigit():
    print('ERROR')
    exit()

args = sys.argv[1]

if __name__ == '__main__':
    st = args.translate(str.maketrans('', '', string.punctuation))
    work = st.split()
    for x in work.copy():
        if len(x) <= int(sys.argv[2]):
            work.remove(x)
    print(work)
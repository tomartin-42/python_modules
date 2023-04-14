import argparse
import string

parser = argparse.ArgumentParser(description = 'removes all the words in a string that are shorter than or equal to n letters')
parser.add_argument('string', type = str, nargs='?', default=None)
parser.add_argument('number', type = int, nargs='?', default=None)

args = parser.parse_args()

if args.string is None or args.number is None:
    print('ERROR')
    exit()

if __name__ == '__main__':
    st = args.string.translate(str.maketrans('', '', string.punctuation))
    work = st.split()
    for x in work.copy():
        if len(x) <= args.number:
            work.remove(x)
    print(work)
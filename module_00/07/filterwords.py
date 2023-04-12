import argparse
import string

parser = argparse.ArgumentParser(description = 'removes all the words in a string that are shorter than or equal to n letters')
parser.add_argument('string', type = str)
parser.add_argument('number', type = int)
args = parser.parse_args()

if __name__ == '__main__':
    st = args.string.translate(str.maketrans('', '', string.punctuation))
    work = st.split()
    print(work)
    for x in work:
        print(x, "->", len(x))
        if len(x) <= args.number:
            work.remove(x)
    print(work)

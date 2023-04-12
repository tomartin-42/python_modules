import sys


def rev_swap(args):
    res = ' '.join(args)
    res = res[::-1].swapcase()
    return res


if __name__ == '__main__':
    res = rev_swap(sys.argv[1:])
    print(res)

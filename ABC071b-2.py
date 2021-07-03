import string
from collections import Counter


def main():
    # S = 'abcdefghijklmnopqrstuvwxyz'
    S = int(input())
    bucket = Counter(S)
    for alphabet in string.ascii_lowercase:
        if bucket.get(alphabet) is None:
            print(alphabet)
            exit()
    print('None')


if __name__ == '__main__':
    main()

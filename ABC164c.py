import string


def main():
    S = 'atcoderregularcontest'

    s = set(S)

    print(s)

    for alphabet in string.ascii_lowercase:
        if alphabet not in s:
            print(alphabet)
            exit()
    print('None')


if __name__ == '__main__':
    main()

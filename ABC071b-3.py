import string


def main():
    S = str(input())
    s_ = set(S)
    for alpha in string.ascii_lowercase:
        if alpha not in s_:
            print(alpha)
            exit()
    print('None')


if __name__ == '__main__':
    main()

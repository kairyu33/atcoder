import string


def main():
    S = 'abcdefghijklmnopqrstuvwxyz'
    bucket = dict()
    for c in S:
        if bucket.get(c):
            bucket[c] += 1
        else:
            bucket[c] = 1
    print(bucket)
    for alphabet in string.ascii_lowercase:
        if bucket.get(alphabet) is None:  # バケット内にそのアルファベットがない場合
            print(alphabet)
            exit()
    print('None')


if __name__ == '__main__':
    main()

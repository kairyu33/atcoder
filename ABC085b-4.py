from collections import Counter


def main():
    N = int(input())
    D = [int(input()) for _ in range(N)]
    bucket = Counter(D)
    print(len(bucket))


if __name__ == '__main__':
    main()

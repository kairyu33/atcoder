from collections import Counter


def main():
    N = int(input())
    A = list(map(int, input().split()))
    bk = Counter(A)

    for i in range(1, N + 1):
        print(bk[i])


if __name__ == '__main__':
    main()

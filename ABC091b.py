import collections


def main():
    N = int(input())
    S = []
    for _ in range(N):
        S.append(input())

    M = int(input())
    T = []
    for _ in range(M):
        T.append(input())

    bucket_S = collections.Counter(S)
    bucket_T = collections.Counter(T)
    if not bucket_S - bucket_T:
        print(0)
    else:
        print((bucket_S - bucket_T).most_common()[0][1])


if __name__ == '__main__':
    main()

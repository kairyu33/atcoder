def main():
    N = int(input())
    A = [int(x) for x in input().split()]
    B = [int(x) for x in input().split()]
    C = [int(x) for x in input().split()]
    B2 = []
    ans = 0
    for j in range(N):
        B2 = [i for i, x in enumerate(B) if x == A[j]]
        for x in range(len(B2)):
            tmp = B2[x] + 1
            ans = C.count(tmp) + ans
    print(ans)


if __name__ == '__main__':
    main()

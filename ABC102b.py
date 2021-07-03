def main():
    N = int(input())
    A = []
    max_diff = 0
    for a in input().split():
        A.append(int(a))

    for i in range(N):
        for j in range(i + 1, N):
            max_diff = max(max_diff, abs(A[i] - A[j]))

    print(max)


if __name__ == '__main__':
    main()

def main():
    N, K = map(int, input().split())
    A = [int(x) for x in input().split()]
    okashi_count = int(K / N)
    okashi_amari = K % N

    for i in range(len(A)):
        if (A[i] <= okashi_amari + 1):
            print(okashi_count + 1)
        else:
            print(okashi_count)


if __name__ == '__main__':
    main()

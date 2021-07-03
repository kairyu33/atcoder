def main():
    N = int(input())
    A = [int(x) for x in input().split()]

    ld = sorted(A, reverse=True)
    alice = 0
    bob = 0
    for i in range(len(A)):
        if i % 2 == 0:
            alice = ld[i] + alice
        else:
            bob = ld[i] + bob
    print(alice - bob)


if __name__ == '__main__':
    main()

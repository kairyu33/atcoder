def main():
    N = int(input())
    A = sorted([abs(int(i)) for i in input().split()])

    print(sum(A))
    print(sum([a ** 2 for a in A]) ** 0.5)
    print(max(A))


if __name__ == '__main__':
    main()

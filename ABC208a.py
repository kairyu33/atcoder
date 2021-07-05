def main():
    A, B = map(int, input().split())
    count = 0
    sum = 0
    for i in range(A):
        for j in range(1, 7):
            if sum + j == B:
                count += 1
        sum = sum + 6

    if count >= 1:
        print('Yes')
    else:
        print('No')

    print(count)


if __name__ == '__main__':
    main()

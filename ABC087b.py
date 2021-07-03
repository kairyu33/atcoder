def main():
    A = int(input())
    B = int(input())
    C = int(input())
    D = int(input())

    count = 0

    for a in range(0, A + 1):
        for b in range(0, B + 1):
            for c in range(0, C + 1):
                amount = 500 * a + 100 * b + 50 * c

                if amount == D:
                    count += 1

    print(count)


if __name__ == '__main__':
    main()

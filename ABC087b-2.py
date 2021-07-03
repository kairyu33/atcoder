def main():
    A = int(input())
    B = int(input())
    C = int(input())
    D = int(input())

    count = 0

    total_money = 500 * A + 100 * B + 50 * C
    if total_money >= 500:
        count = loop3(A, B, C, D)
    elif total_money >= 100:
        count = loop2(B, C, D)
    else:
        count = not_loop(C, D)
    print(count)


def loop3(A, B, C, D):
    count = 0
    for a in range(0, A + 1):
        for b in range(0, B + 1):
            for c in range(0, C + 1):
                amount = 500 * a + 100 * b + 50 * c
                if amount == D:
                    count += 1
    return count


def loop2(B, C, D):
    count = 0
    for b in range(0, B + 1):
        for c in range(0, C + 1):
            amount = 100 * b + 50 * c
            if amount == D:
                count += 1
    return count


def not_loop(C, D):
    count = 0
    amount = 50 * C
    if amount == D:
        count += 1
    return count


if __name__ == '__main__':
    main()

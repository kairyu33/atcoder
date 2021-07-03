def 各桁の和を求める(i):
    total = 0
    while i > 0:
        total += i % 10
        i //= 10
    return total


def main():
    # N, A, B = map(int, input().split())
    # print(N, A, B)
    N, A, B = 20, 2, 5
    total = 0
    for i in range(1, N + 1):
        # ある整数 i の各桁の和を求める
        digit_sum = 各桁の和を求める(i)
        if A <= digit_sum <= B:
            # 10進法での各桁の和がA以上B以下であるときに加算していく
            total += i
    print(total)


if __name__ == '__main__':
    main()

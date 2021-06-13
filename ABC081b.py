def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 10000000000
    # それぞれ整数がどれだけ2で割れるかを調べる
    for a in A:
        count = 0
        while a % 2 == 0:
            count += 1
            a = a // 2
        ans = min(ans, count)
    print(ans)
    count = 0


if __name__ == '__main__':
    main()

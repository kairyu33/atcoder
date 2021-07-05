def main():
    N = int(input())
    # リスト内包表記
    # 上から順にlistを読み込んでlistに格納していく。
    a = [list(map(int, input().split())) for N in range(N)]
    if a[0][0] == 1:
        print(a[0][2] - a[0][1])
    print(a[0])


if __name__ == '__main__':
    main()

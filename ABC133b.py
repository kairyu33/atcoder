import math


def Range(pA, pB, d):
    z = 0
    for i in range(d):
        z = (pA[i] - pB[i]) ** 2 + z
    z = math.sqrt(z)
    return (z)


def main():
    ans = 0
    # 点の個数と次元を入力
    p_count, dimension = map(int, input().split())
    # 点の座標情報入力・格納
    l = [list(map(int, input().split())) for l in range(p_count)]

    for i in range(p_count):
        if (p_count - 1 == i):
            # 判定処理
            if (Range(l[i], l[0], dimension).is_integer() == True):
                ans = ans + 1
        else:
            # 判定処理
            if (Range(l[i], l[i + 1], dimension).is_integer() == True):
                ans = ans + 1

    # 整数の数_算出
    if (dimension == 1):
        ans = ans * 2
    print(ans)


if __name__ == '__main__':
    main()

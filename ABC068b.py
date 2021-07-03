def main():
    N = int(input())
    count_max = 1  # 割る回数最大値格納用
    max_num = 1  # 一番割り切れる数字格納用
    for i in range(1, N + 1):
        count = 0
        nam = i + 1
        while nam % 2 == 0:
            count += 1
            nam = nam / 2  # num /= 2 なるべく整数で扱う（小数[浮動小数点]は避ける）
        if max_num <= count:
            max_num = count
            countMax = i + 1

    print(countMax)


if __name__ == '__main__':
    main()

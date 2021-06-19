def main():
    N = int(input())
    countMax = 1  # 一番大きな数字格納用
    MaxNam = 1  # 整数格納用
    for i in range(N):
        count = 0
        nam = i + 1
        while nam % 2 == 0:
            count += 1
            nam = nam / 2
        if (MaxNam <= count):
            MaxNam = count
            countMax = i + 1

    print(countMax)


if __name__ == '__main__':
    main()

def main():
    r, g, b = map(int, input().split())
    n = r * 100 + g * 10 + b * 1

    if n % 4 == 0:
        print('YES')
    else:
        print('NO')


if __name__ == '__main__':
    main()

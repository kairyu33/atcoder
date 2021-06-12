def main():
    a, b = map(int, input().split())
    print(a, b)

    if a * b % 2:
        c = 'Odd'
    else:
        c = 'Even'
    print(c)


if __name__ == '__main__':
    main()

def main():
    a, b = map(int, input().split())

    if a * b % 2:
        c = 'Odd'
    else:
        c = 'Even'
    print(c)


if __name__ == '__main__':
    main()

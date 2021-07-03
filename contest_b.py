def main():
    a, b, c, d = map(int, input().split())
    blue = a
    red = 0
    num = 0
    while blue >= red * d:
        if blue <= red * d:
            break
        elif num > 100000:
            num = -1
            break
        else:
            blue = b + blue
            red = c + red
            num += 1
    print(num)


if __name__ == '__main__':
    main()

def main():
    N = int(input())
    count = 0
    sum = 0
    while sum < N:
        count += 1
        sum = count + sum

    print(count)


if __name__ == '__main__':
    main()

def main():
    N = int(input())
    D = [int(input()) for _ in range(N)]
    # 整数バケット
    bucket = [0] * 101
    for d in D:
        bucket[d] += 1
    count = 0
    for v in bucket:
        if v > 0:
            count += 1
    print(count)


if __name__ == '__main__':
    main()

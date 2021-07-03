def main():
    N = int(input())
    D = [int(input()) for _ in range(N)]
    bucket = dict()
    for d in D:
        if bucket.get(d):
            bucket[d] += 1
        else:
            bucket[d] = 1
    print(len(bucket))


if __name__ == '__main__':
    main()

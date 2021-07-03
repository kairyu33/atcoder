def main():
    N = int(input())
    d_list = list()
    for i in range(1, N + 1):
        d = int(input())
        d_list.append(d)
    print(len(set(d_list)))


if __name__ == '__main__':
    main()

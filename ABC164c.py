
def main():
    N = int(input())
    A = []
    for _ in range(N):
        A.append((input()))

    print(len(set(A)))

if __name__ == '__main__':
    main()

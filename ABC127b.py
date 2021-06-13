def tmp(r, D, x_):
    z = r * x_ - D
    return (z)


def main():
    r, D, x = map(int, input().split())
    for i in range(10):
        print(tmp(r, D, x))
        x = tmp(r, D, x)


if __name__ == '__main__':
    main()

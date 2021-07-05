import math


def main():
    P = int(input())
    pr = []
    for i in range(1, 11):
        pr.append(math.factorial(i))
    sum = P
    count = 0
    while sum > 0:
        for i in range(1, 11):
            if sorted(pr)[-i] <= sum:
                sum = sum - sorted(pr)[-i]
                count += 1
                break

    print(count)


if __name__ == '__main__':
    main()

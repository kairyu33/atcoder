# 入力
# N
# x1 ... xn

N = int(input())
X = [int(x) for x in input().split()]

# 入力
# N M
# A1
# A2
#:
# AN
N, M = map(int, input().split())
A = []
for _ in range(M):
    A.append(int(input()))

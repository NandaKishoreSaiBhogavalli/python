n = int(input().strip())

M = set(map(int, input().strip().split()))

m = int(input().strip())

N = set(map(int, input().strip().split()))

A = M.symmetric_difference(N)
so = sorted(A)
for i in so:
    print(i)
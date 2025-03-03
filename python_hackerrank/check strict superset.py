A = set(map(int, input().strip().split()))
N = int(input().strip())
otherset = []
for i in range(N):
    n = set(map(int, input().strip().split()))
    otherset.append(n)

superset = all(A.issuperset(n) and len(A) > len(n) for n in otherset)
print(superset)
N, M = map(int, input().split())

# Top half pattern
for i in range(N // 2):
    pattern = ".|." * (2 * i + 1)
    print(pattern.center(M, "-"))

# Middle 'WELCOME' line
print("WELCOME".center(M, "-"))

# Bottom half pattern (reverse of top half)
for i in range(N // 2 - 1, -1, -1):
    pattern = ".|." * (2 * i + 1)
    print(pattern.center(M, "-"))
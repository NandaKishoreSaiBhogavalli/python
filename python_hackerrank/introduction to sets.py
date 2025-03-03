def average(array):
    unique = set(array)
    sums = sum(unique)
    count = len(unique)
    avg = sums / count
    avg_rounded = round(avg, 3)
    return avg_rounded


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
cube = lambda x: x**3

def fibonacci(n):
    # return a list of fibonacci numbers
    fiblist = []
    a,b = 0,1
    for i in range(n):
        fiblist.append(a)
        a,b = b,a+b
    return fiblist

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
def solve(s):
    list = []
    for i in s.split(" "):
        list.append(i.capitalize())
    return " ".join(list).strip()
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
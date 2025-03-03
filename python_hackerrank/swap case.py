def swap_case(s):
    results = ""
    for char in s:
        if char.islower():
            char = char.upper()
            results += char
        elif char.isupper():
            char = char.lower()
            results += char
        else:
            results += char
    return results

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
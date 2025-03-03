n = int(input().strip())
unique = set()
words = []
word_count = {}
for i in range(n):
    N = input().strip()
    unique.add(N)
    words.append(N)

for word in words:
    word_count[word] = word_count.get(word, 0) + 1
value_list = list(word_count.values())
strng = " ".join(map(str, value_list))
print(len(unique))
print(strng)
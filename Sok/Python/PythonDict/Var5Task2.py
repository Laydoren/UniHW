text = [word for _ in range(int(input("Num of lines: "))) for word in input().split()]

dic_words = {word : text.count(word) for word in set(text)}

l_words = [(count, word) for word, count in dic_words.items()]

result = sorted(l_words, key=lambda word: (-word[0], word[1]))

for freq, word in result: print(f"'{word}'({freq})", end=", ")

# test text (ctr+c, ctr+v)
# {
#     hi
#     hi
#     what is your name
#     my name is bond
#     james bond
#     my name is damme
#     van damme
#     claude van damme
#     jean claude van damme
# }
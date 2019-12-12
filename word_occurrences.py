

text = input("Text: ")
count_word = {}
word = text.split()
for i in word:
    count_word[i] = count_word.get(i, 0)+1
word =list(count_word)
word.sort()
max_length = max((len(i) for i in word))
for i in word:
    print("{:{}} : {}".format(i, max_length, count_word[i]))
input_text = input("Enter the Text : ").lower()
word_list = input_text.split()
word_count = dict()
for word in word_list:
    if word not in word_count:
        word_count[word] = 1
    else:
        word_count[word] += 1
for word in word_count:
    print(f"{word} : \t{word_count[word]}")
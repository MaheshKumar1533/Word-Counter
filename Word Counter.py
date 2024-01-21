input_text = input("Enter the Text : ").lower() # take input and convert to lower case
word_list = input_text.split() # split the input into a list of words
word_count = dict()
for word in word_list:
    if word not in word_count:
        word_count[word] = 1 # add the word if it is not present
    else:
        word_count[word] += 1 # increment count by one if its present
for word in word_count:
    print(f"{word} : \t{word_count[word]}") # print word frequency

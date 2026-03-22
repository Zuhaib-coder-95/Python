def match_words(words):

    count = 0
    newlist = []
    for word in words:
        if len (word) > 1 and word [0] == word[-1]:
            count += 1
            newlist.append(word)

output = match_words(['abc', 'cfc', 'xyz','aba', '1221'])
print("Number of words having first and last character same:", output)

def fuction(words):
    ctr = 0
    list = []
    for word in words:
        if len(word) > 2 and word[0] == word[-1]:
            ctr += 1
            list.append(word)
    print(" List of words with first and last letter: ", list)

    return ctr

count = fuction(['abc', 'cfc', 'xyz', 'aba', '1221'])
print(" number of words having first and last letter: ", count)
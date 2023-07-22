def capitals(word):
    ordered_list = []
    for index in range(len(word)): # iterating through the string
        if word[index].isupper(): # checking condition
            ordered_list.append(index) # adding the index to the list if condition is True
    return ordered_list
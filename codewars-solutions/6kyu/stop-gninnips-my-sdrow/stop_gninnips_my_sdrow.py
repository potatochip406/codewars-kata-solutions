def spin_words(sentence):
    str_list = sentence.split(' ')
    new_list = []
    for str in str_list:
        if len(str) >= 5:
            new_list.append(str[::-1]) # reversing the string
        else:
            new_list.append(str)
            
    s = ' '.join(new_list)
    return s
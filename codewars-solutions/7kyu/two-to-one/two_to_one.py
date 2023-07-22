def longest(a1, a2):
    distinct_letters = []
    # using ASCII values to iterate through the alphabet
    # although chr(122) == 'z', i did 123 because a for range loop is exclusive of the outer bound
    for x in range(97, 123):
        char = str(chr(x))
        if char in a1 or char in a2: # checking if the current letter is in either string
            distinct_letters.append(char)
    return "".join(distinct_letters) # concatenating each distinct letter into a single string to be returned

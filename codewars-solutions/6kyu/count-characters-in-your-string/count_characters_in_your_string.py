def count(string):
    dictionary = {}
    for character in string:
        dictionary.update({character: string.count(character)})
    return dictionary

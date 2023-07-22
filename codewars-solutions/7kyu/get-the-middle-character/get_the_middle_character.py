def get_middle(string):
    x = len(string)
    if len(string) % 2 == 0:
        return string[(x // 2) - 1] + string[x // 2]
    else:
        return string[x//2]
def square_digits(num):
    final_str = ""
    str_num = str(num)
    for index in range(0, len(str_num)):
        final_str += str(int(str_num[index]) ** 2)
    return int(final_str)

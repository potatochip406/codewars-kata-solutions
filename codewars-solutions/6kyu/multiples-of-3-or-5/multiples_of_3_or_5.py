def solution(number):
    if number >= 0:
        final_sum = 0
        for x in range(number - 1, 0, -1):
            if x % 5 == 0 or x % 3 == 0:
                final_sum += x
        return final_sum
    else:
        return 0

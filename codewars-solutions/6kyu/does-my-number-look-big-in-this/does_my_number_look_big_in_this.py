def narcissistic( value ):
    # converting the value to a string to get its digit amount
    string_value = str(value)
    digit_amount = len(string_value)
    
    # creating an empty digit list and adding the integer value of each digit into the list
    individual_digits = []
    for val in range(digit_amount):
        individual_digits.append(int(string_value[val]))

    # iterating through the digit list and adding the calculated values to the `final_sum` variable to be checked
    final_sum = 0
    for num in individual_digits:
        final_sum += pow(num, digit_amount)
        
    # checking the final condition
    if final_sum == value:
        return True
    else:
        return False
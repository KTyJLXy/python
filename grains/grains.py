def square(number):
    if number <= 0 or number > 64:
        raise ValueError("Square number can't be a negative or Zero or >64")
    return 2 ** (number - 1)


def total(number):
    if number <= 0 or number > 64:
        raise ValueError("Square number can't be a negative or Zero or >64")
    #Vars
    total_number = 0
    i = 1
    
    while i <= number:
        total_number += square(i)
        i += 1
    
    return total_number

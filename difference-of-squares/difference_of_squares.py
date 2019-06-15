def square_of_sum(number):
    plain_sum = 0
    while number > 0:
         plain_sum += number
         number -= 1
    square_sum = plain_sum **2
    return square_sum
    
def sum_of_squares(number):
    sum_square = 0
    while number > 0:
         sum_square += number **2
         number -= 1
    return sum_square


def difference_of_squares(number):
    return square_of_sum(number) - sum_of_squares(number) 
    

def classify(number):
    
    if number <= 0:
        raise ValueError('Should not be Zero or negative')
    
    status = ''
    
    if sum(get_factors_list(number)[:-1]) > number:
        status = 'abundant'
    if sum(get_factors_list(number)[:-1]) == number:
        status = 'perfect'
    if sum(get_factors_list(number)[:-1]) < number:
        status = 'deficient'
    
    return status

def get_factors_list(number):
    
    factors = [i for i in range(1, number + 1) if number % i == 0]
    
    return factors
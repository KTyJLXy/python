def factors(value):
    #Vars
    i = 2
    prime_factors = []
    #Getting prime_factors list
    while i * i <= value:
        if value % i:
            i += 1
        else:
            value //= i
            prime_factors += [i] 
    
    if value > 1:
        prime_factors += [value]
        
    return prime_factors

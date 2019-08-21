def largest(min_factor, max_factor):
    start = min_factor
    stop = max_factor
    if start > stop or start < 0 or stop < 0:
        raise ValueError("Wrong range")
    #Vars
    numbers = []
    factr = {}

    
    for j in range(start, stop+1):
        for n in range(start, stop+1):
            if str(n * j) == str(n * j)[::-1]:
                numbers += [n * j]
                try:
                    factr[n * j]= factr[n * j], [n,j]
                except:
                    factr[n * j]= [n,j]
    tupl = (max(numbers),factr[max(numbers)])
    return tupl

def smallest(min_factor, max_factor):
    start = min_factor
    stop = max_factor
    if start > stop or start < 0 or stop < 0:
        raise ValueError("Wrong range")
    #Vars
    numbers = []
    factr = {}
    
    for j in range(start, stop+1):
        for n in range(start, stop+1):
            if str(n * j) == str(n * j)[::-1]:
                numbers += [n * j]
                factr[n * j]= [n,j]
    tupl = (min(numbers),factr[min(numbers)])
    return tupl

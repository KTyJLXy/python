def is_armstrong_number(number):
    #Vars
    listing = str(number)
    mult = len(listing)
    summing = 0
    
    for chr in listing:
        summing += int(chr) ** mult
    if summing == number:
        return True
    return False
    pass

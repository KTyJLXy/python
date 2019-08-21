def convert(number):
    #Vars
    strings = {3:"Pling", 5:"Plang", 7:"Plong"}
    #Get factors for a given number
    factors = [i for i in range(1, number + 1) if number % i == 0]
    #Check for factors we need and generate raindrop
    raindrop = [strings[number] for number in factors if number in strings]
    #If no dict factors return a number as a str
    if len(raindrop) == 0:
        raindrop = str(number)
    return ''.join(raindrop)
           

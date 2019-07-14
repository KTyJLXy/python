def convert(number):
    #Vars
    factors = []
    strings = {3:"Pling", 5:"Plang", 7:"Plong"}
    raindrop = ""
    #Get factors for a given number
    for i in range(1, number + 1):
       if number % i == 0:
           factors += [i]
    #Check for factors we need and generate raindrop
    for number in factors:
        if number in strings:
            raindrop += strings[number]
    #If no dict factors return a number as a str
    if raindrop == "":
        return str(number)
    return raindrop
           

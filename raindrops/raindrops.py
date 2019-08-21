def convert(number):
    #Vars
    drops = [(3,"Pling"),(5,"Plang"),(7,"Plong")]
    raindrop = [sound for num, sound in drops if number % num == 0]
    #If no dict factors return a number as a str
    return str(number) if len(raindrop) == 0 else ''.join(raindrop)
           

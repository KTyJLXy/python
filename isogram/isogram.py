def is_isogram(string):
    temp = string.lower()
    for letter in temp:
        if temp.count(letter) > 1 and letter.isalnum() == True: 
            return False
    return True
    

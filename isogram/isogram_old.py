def is_isogram(string):
        
    letter_list = []
    result = True
    
    for letter in string.lower():
        if letter.isalnum():
            if letter in letter_list: 
                result = False
                break
            else: 
                letter_list.append(letter)
    
    return result
    

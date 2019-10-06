import collections

def is_isogram(string):
    result = True
    for letter in string.lower():
        if collections.Counter(string.lower())[letter] > 1 and letter.isalnum() == True:
            result = False
    return result
    

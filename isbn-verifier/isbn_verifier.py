#Calculate processed ISBN string
def check_isbn(isbn_str):
        
    multiplayer = 10
    isbn_sum = 0
        
    for char in isbn_str:
        if char == 'X':
            isbn_sum += 10 * multiplayer
            multiplayer -= 1
        else:
            isbn_sum += (int(char) * multiplayer)
            multiplayer -= 1 
    if isbn_sum % 11 == 0 and len(isbn_str) == 10:
        return True
    else:
        return False
#Validate processed ISBN string    
def check_symbols(isbn_str):
        if len(isbn_str) != 10:
            return False
        elif isbn_str[9] not in "123456789X":
            return False
        else:
            try:
                int(isbn_str[0:9])
            except:
                return False
            return True
            
def is_valid(isbn):
    
    # formula (x1 * 10 + x2 * 9 + x3 * 8 + x4 * 7 + x5 * 6 + x6 * 5 + x7 * 4 + x8 * 3 + x9 * 2 + x10 * 1) mod 11 == 0
    
    if '-' in isbn:
        isbn = ''.join(isbn.split('-'))
        if check_symbols(isbn) == True:
            return check_isbn(isbn)
        else:
            return False
    # Split   
    elif '-' not in isbn:
        if check_symbols(isbn) == True:
            return check_isbn(isbn)
        else:
            return False
    # Split
    elif len(isbn) == 0:
        return False
    

        
        
        

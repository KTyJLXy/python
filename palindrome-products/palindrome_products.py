def largest(min_factor, max_factor):
    
    palindrome = {}
    
    for i in range(min_factor, max_factor + 1):
        for j in range(min_factor, max_factor + 1):
            if str(i*j) == str(i*j)[::-1]:
                palindrome[i*j] = [i,j]
                
    return (max(palindrome),palindrome[max(palindrome)])

def smallest(min_factor, max_factor):
        for i in range(min_factor, max_factor + 1):
            for j in range(min_factor, max_factor + 1):
                if str(i*j) == str(i*j)[::-1]:
                    return ((i*j),[i,j])

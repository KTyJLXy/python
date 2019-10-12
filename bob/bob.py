def response(hey_bob):
    
    answer = ""
    clear_line = hey_bob.rstrip()
    
    
    if len(clear_line) == 0:
        answer = "Fine. Be that way!"
    elif clear_line[-1] == "?" and hey_bob.isupper() == True:
        answer = "Calm down, I know what I'm doing!"  
    elif clear_line[-1] == "?":
        answer = "Sure."
    elif clear_line.isupper() == True:
        answer = "Whoa, chill out!"
    else:
        answer = "Whatever."
    return answer
def is_isogram(string):
    temp = string.lower()
    return all(temp.count(c) == 1 for c in temp if c. isalnum())

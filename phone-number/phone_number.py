class Phone(object):
    
    def __init__(self, phone_number):
        #Attributes
        self.number = self.number_clear(phone_number)
        self.area_code = self.number[0:3]
    
    def number_clear(self, number):
        
        clean_number = ""
        
        for char in number:
            if char.isdigit() == True:
                clean_number += char
                
        if len(clean_number) > 11:
            raise ValueError("Invalid number")
        
        if clean_number[0] != '1' and len(clean_number) == 11:
            raise ValueError("Invalid number")
        
        if clean_number[0] == '1' and len(clean_number) == 11:
            clean_number = clean_number[1:]
            
        if int(clean_number[0]) < 2 or int(clean_number[3]) < 2:
            raise ValueError("Invalid number")
        
        return clean_number
    
    def pretty(self):
        return f"({self.area_code}) {self.number[3:6]}-{self.number[6:10]}"
        
        
class Phone(object):
    
    def __init__(self, phone_number):
        #Attributes
        self.number = self.number_clear(phone_number)
        self.area_code = self.number[0:3]
        
    def number_clear(self, phone_number):
        #Vars
        number = []
        
        for char in phone_number:
            if char.isdigit() == True:
                number += char
        
        if len(number) < 10:
            raise ValueError('Invalid number')
            
        if number[0] == 1:
            number = number[1:]
        
        if number[0] not in range(2,10):
            if len(number) == 11:
                number = number[1:]
            else:
                raise ValueError('Invalid number')
                
        if number[3] not in range(2,10):
            raise ValueError('Invalid number')
        
        return ''.join(number)
    
    #def pretty(self):
        
    
    
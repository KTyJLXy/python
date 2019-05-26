import string, random
# namelist
names = []
#robot_object
class Robot:
    #initialisation
    def __init__(self):
        self.name = self.robot_name()
        self.reset()
    #generate name
    def robot_name(self):
        alphabet = string.ascii_uppercase
        digits = string.digits

        first_two = [random.choice(alphabet) for n in range(2)]
        last_bits = [random.choice(digits) for n in range(3)]
        self.name = "".join(first_two + last_bits)
        return self.name
    #reset method
    def reset(self):
        if self.name not in names:
            names.append(self.name)
        else:
            self.name = self.robot_name()
            self.reset()
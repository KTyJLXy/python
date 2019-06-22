import random, math

class Character:
    
    def __init__(self):
        #Stats
        self.strength = self.random_stat()
        self.dexterity = self.random_stat()
        self.constitution = self.random_stat()
        self.intelligence = self.random_stat()
        self.wisdom = self.random_stat()
        self.charisma = self.random_stat()

        #Hitpoints
        self.hitpoints = 10 + modifier(self.constitution)
        
    def ability(self):
       return random.choice([self.strength, self.dexterity, self.constitution, self.intelligence, self.wisdom, self.charisma])
    
    def random_stat(self):
        #Vars
        i = 0
        stat_sum = []
        
        while i <= 3:
            stat_sum = stat_sum + [random.randint(1,6)]
            i = i + 1
        del stat_sum[stat_sum.index(min(stat_sum))]
        return sum(stat_sum)
    
def modifier(n):
    mod = math.floor((n - 10) / 2)
    return mod
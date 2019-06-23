# Game status categories
# Change the values as you see fit
STATUS_WIN = "win"
STATUS_LOSE = "lose"
STATUS_ONGOING = "ongoing"


class Hangman(object):
    def __init__(self, word):
        #Vars
        self.remaining_guesses = 9
        self.status = STATUS_ONGOING
        self.letters = []
        self.masked_word = ""
        self.word = word
        i = 1
        #Generate masked word
        while i <= len(word):
            self.masked_word += "_" 
            i += 1

    def guess(self, char):
        #Check if game is won or no guesses left
        if self.remaining_guesses < 0:
            self.status = STATUS_LOSE
            raise ValueError ('The game has ended')
        
        if self.status == STATUS_WIN:
           raise ValueError ('The game has ended')
            
        if char in self.letters:
            self.remaining_guesses -= 1   
        
        self.letters += [char]
        #Unmask letters if correct
        if char in self.word:
            self.indexlist = []
            for idx, val in enumerate(self.word):
                if val == char:
                    self.indexlist += [idx] 

            self.masked_word = list(self.masked_word)
            
            for index in self.indexlist:
                self.masked_word[index] = char 
            
            self.masked_word = ''.join(self.masked_word)
        #Check if won
        if '_' not in self.masked_word:
            self.status = STATUS_WIN
        #Check for decrement
        if self.status != STATUS_LOSE and self.status != STATUS_WIN and char not in self.word:
            self.remaining_guesses -= 1   
        #Check if there are any guesses left
        if self.remaining_guesses <= 0 and self.status != STATUS_WIN:
            self.status = STATUS_LOSE
               
    def get_masked_word(self):
        return self.masked_word

    def get_status(self):
        return self.status

class round:
    
    def __init__(self, manual = True):
        self.roll_num = 0
        self.manual = True
        self.round_score = 0

        self.game_over = False

        


    def add_score(self, roll):
        
        if self.roll_num <= 3:

            if roll == 7:
                self.round_score += 70
            else:
                self.round_score += roll


            self.roll_num +=1 ## add score
        else:

            if roll == "double":
                self.round_score = self.round_score * 2
            
            elif roll == 7:
                self.round_score = 0

                self.game_over = True
            
            else:
                self.round_score += roll
        
    def get_score(self):
        return self.round_score
    
    def get_game_over(self):
        return self.game_over
    
    def get_roll_num(self):
        return self.roll_num



class player:
    
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.banked = False



    
    def bank_score(self, value):
        self.score = self.score + value
        self.banked = False
    
    def get_score(self):
        return self.score

    def reset(self):
        self.score = 0

    def get_banked(self):
        return self.banked
    
    def set_not_banked(self):
        self.banked = False
    
    def get_name(self):
        return self.name
    
    

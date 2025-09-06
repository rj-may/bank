class player:
    
    def __init__(self, name):
        self.name = name
        self.score = 0
    
    def bank_score(self, value):
        self.score = self.score + value
    
    def get_score(self):
        return self.score

    def reset(self):
        self.score = 0
    

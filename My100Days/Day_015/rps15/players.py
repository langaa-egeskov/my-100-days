class Player:
    def __init__(self, name):
        self.name = name
        self.wins = 0
    
    def __repr__(self):
        return f'Player({self.name})'
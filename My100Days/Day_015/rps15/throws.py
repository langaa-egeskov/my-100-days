class Throw:

    def __init__(self, name, defeated_throws):
        self.name = name
        self.defeated_throws = defeated_throws

    def can_defeat(self, throw):
        if throw.name in self.defeated_throws:
            return True
        else:
            return False
        
    def __repr__(self):
        return f'Throw({self.name}, {self.defeated_throws})'
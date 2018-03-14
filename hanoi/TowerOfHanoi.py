from hanoi.Stack import Stack


class TowerOfHanoi:
    
    def __init__(self, numberOfDisks):
        self.rods = [Stack(numberOfDisks), Stack(), Stack()]
        self.turnCount = 0
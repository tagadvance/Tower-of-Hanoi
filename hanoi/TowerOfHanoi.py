from hanoi.Stack import Stack


class TowerOfHanoi:
    
    def __init__(self, numberOfDisks):
        self.rods = [Stack(numberOfDisks), Stack(), Stack()]
        self.turnCount = 0
    
    def shiftDisk(self, fromRod, toRod):
        self.turnCount += 1
        
        disk = fromRod.removeDisk()
        toRod.addDisk(disk)
    
    def isSolved(self):
        emptyCount = 0
        for rod in self.rods:
            if not rod:
                emptyCount += 1
        
        # First rod is empty, and only one rod IS NOT empty.
        return not self.rods[0] and emptyCount == len(self.rods) - 1
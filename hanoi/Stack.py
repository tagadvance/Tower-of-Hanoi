from hanoi.Disk import Disk
from hanoi.HanoiException import HanoiException


class Stack:
    '''
    Note: _stack[0] indicates the bottom of the stack.
    '''
    
    def __init__(self, numberOfDisks=0):
        self._stack = []
        
        for i in reversed(range(numberOfDisks)):
            disk = Disk(i)
            self._stack.append(disk)
    
    def __bool__(self):
        return self._stack.__bool__()
    
    def mayAddDisk(self, disk):
        if self._stack:
            topDisk = self._stack[-1]
            if disk > topDisk:
                return False
        return True
        
    def addDisk(self, disk):
        if not self.mayAddDisk(disk):
            raise HanoiException('No disk may be placed on top of a smaller disk.')
        
        self._stack.append(disk)
    
    def removeDisk(self):
        return self._stack.pop() if self._stack else None
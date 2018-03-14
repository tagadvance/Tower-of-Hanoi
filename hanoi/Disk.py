class Disk:
    
    def __init__(self, size):
        self.size = size

    def __gt__(self, other):
        return self.size > other.size if isinstance(other, Disk) else False

    def __le__(self, other):
        return self.size < other.size if isinstance(other, Disk) else False
    
    def __eq__(self, other):
        return self.size == other.size if isinstance(other, Disk) else False
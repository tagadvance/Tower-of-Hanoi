from hanoi.TowerOfHanoi import TowerOfHanoi
import unittest


class TestStack(unittest.TestCase):

    def test_TowerOfhanoi(self):
        '''
        https://upload.wikimedia.org/wikipedia/commons/6/60/Tower_of_Hanoi_4.gif
        '''
        
        numberOfDisks = 4
        toh = TowerOfHanoi(numberOfDisks)
        
        moves = [
            (0, 1),
            (0, 2),
            (1, 2),
            (0, 1),
            (2, 0),
            (2, 1),
            (0, 1),
            (0, 2),
            (1, 2),
            (1, 0),
            (2, 0),
            (1, 2),
            (0, 1),
            (0, 2),
            (1, 2),
        ]
        for move in moves:
            self.assertFalse(toh.isSolved())
            
            fromIndex, toIndex = move
            toh.shiftDisk(toh.rods[fromIndex], toh.rods[toIndex])
            
        self.assertTrue(toh.isSolved())


if __name__ == '__main__':
    unittest.main()
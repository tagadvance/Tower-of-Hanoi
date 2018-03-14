from hanoi.Disk import Disk
from hanoi.HanoiException import HanoiException
from hanoi.Stack import Stack
import unittest

class TestStack(unittest.TestCase):

    def test_init(self):
        stack = Stack(3)
        
        expected = [
            Disk(2),
            Disk(1),
            Disk(0)
        ]
        self.assertEqual(expected, stack._stack)

    def test_isEmpty(self):
        stack = Stack()
        self.assertTrue(stack.isEmpty())
        
        stack.addDisk(Disk(0))
        self.assertFalse(stack.isEmpty())

    def test_mayAddDisk_withEmptyStack(self):
        stack = Stack()
        
        mayAddDisk = stack.mayAddDisk(Disk(0))
        self.assertTrue(mayAddDisk)

    def test_mayAddDisk_withSmallerDisk(self):
        stack = Stack()
        stack.addDisk(Disk(1))
        
        mayAddDisk = stack.mayAddDisk(Disk(0))
        self.assertTrue(mayAddDisk)

    def test_mayAddDisk_withLargerDisk(self):
        stack = Stack()
        stack.addDisk(Disk(0))
        
        mayAddDisk = stack.mayAddDisk(Disk(1))
        self.assertFalse(mayAddDisk)
    
    def test_addDisk_withEmptyStack(self):
        stack = Stack()
        
        stack.addDisk(Disk(0))
        
        expected = [
            Disk(0)
        ]
        self.assertEqual(expected, stack._stack)

    def test_addDisk_withSmallerDisk(self):
        stack = Stack()
        stack.addDisk(Disk(1))
        
        stack.addDisk(Disk(0))
        expected = [
            Disk(1),
            Disk(0),
        ]
        self.assertEqual(expected, stack._stack)

    def test_addDisk_withLargerDisk(self):
        stack = Stack()
        stack.addDisk(Disk(0))
        
        self.assertRaises(HanoiException, stack.addDisk, Disk(1))
    
    def test_removeDisk_withEmptyStack(self):
        stack = Stack()
        
        self.assertRaises(HanoiException, stack.removeDisk)
        
    def test_removeDisk(self):
        stack = Stack(1)
        actual = stack.removeDisk()
        
        expected = Disk(0)
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()
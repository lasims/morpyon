import unittest
from morpyon_tools import *

class MorpyonTest(unittest.TestCase):
    def test_box_size(self):
        self.assertEqual((1, 1), box_size((3, 3)))
        self.assertEqual((3, 2), box_size((9, 6)))




if __name__ == "__main__":
    unittest.main()

import unittest
from Functions import *

class Testcases(unittest.TestCase):

    def test_distance_point(self):
        self.assertEqual(distance_point(2, 3, 2, 8), 5.0)

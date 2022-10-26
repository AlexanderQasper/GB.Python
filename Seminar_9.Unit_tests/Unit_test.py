import unittest
from Functions import *


class Testcases1(unittest.TestCase):

    def test_distance_point(self):
        self.assertEqual(distance_point(2, 3, 2, 8), 5.0)

    def test_place_dekart1(self):
        self.assertNotEqual(place_dekart(1, 2), 3)

    # Этот, почему-то проходит всегда ОК, хотя вроде должен обрабатывать эксепшен (прописан в функции специально)
    # Этот момент непонятен, гуглёж только
    def test_place_dekart2(self):
        self.assertRaises(TypeError, place_dekart, '4', 3)

    def test_miltiple_arrays_index(self):
        self.assertTrue(type(multiple_arrays_index([1, 2, 3, 4, 5, 6])) == list)


if __name__ == '__main__':
    unittest.main()

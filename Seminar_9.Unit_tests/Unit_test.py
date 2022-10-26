import unittest
from Functions import *


class Testcases(unittest.TestCase):

    # Equal
    def test_distance_point(self):
        self.assertEqual(distance_point(2, 3, 2, 8), 5.0)

    # NotEqual
    def test_place_dekart1(self):
        self.assertNotEqual(place_dekart(1, 2), 3)

    # TypeError
    def test_place_dekart2(self):
        self.assertRaises(TypeError, place_dekart, '4', 3)

    # True
    def test_miltiple_arrays_index(self):
        self.assertTrue(type(multiple_arrays_index([1, 2, 3, 4, 5, 6])) == list)

    # false
    def test_into_binar(self):
        self.assertFalse(type(into_binar(8)) == float)

    # in
    def test_multipliers_num(self):
        self.assertIn(2, multipliers_num(10))

    # IsNot
    def test_delete_str(self):
        self.assertIsNot(delete_str('марат карат забвение квартал абвер'), ['марат', 'карат', 'квартал', 'день'])

    # Is
    def test_min_and_max(self):
        x = min_and_max([1.1, 1.2, 3.1, 5, 10.01])
        y = x
        self.assertIs(x, y)


    # IsNone
    def test_summ_digits(self):
        self.assertIsNone(summ_digits(11))


    # IsNotNone
    def test_orel_reshka(self):
        self.assertIsNotNone(orel_reshka("ОРРОРОРООРРРО"))

if __name__ == '__main__':
    unittest.main()

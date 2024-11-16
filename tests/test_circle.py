import unittest
import math
from circle import area, perimeter

class TestCircle(unittest.TestCase):
    def test_perimeter_positive(self):
        self.assertAlmostEqual(perimeter(5), 2 * math.pi * 5, places=5)
        self.assertAlmostEqual(perimeter(10.5), 2 * math.pi * 10.5, places=5)


    def test_perimeter_edge_cases(self):
        self.assertEqual(perimeter(0), 0)
        self.assertAlmostEqual(perimeter(0.001), 2 * math.pi * 0.001, places=5)

    def test_perimeter_negative(self):
        with self.assertRaises(ValueError):
            perimeter(-5)
        with self.assertRaises(ValueError):
            perimeter(-0.1)


    def test_area_positive(self):
        self.assertAlmostEqual(area(5), math.pi * 5**2, places=5)
        self.assertAlmostEqual(area(10.5), math.pi * 10.5**2, places=5)


    def test_area_edge_cases(self):
        self.assertEqual(area(0), 0)
        self.assertAlmostEqual(area(0.001), math.pi * 0.001**2, places=5)

    def test_area_negative(self):
        with self.assertRaises(ValueError):
            area(-5)
        with self.assertRaises(ValueError):
            area(-0.1)

if __name__ == '__main__':
    unittest.main()
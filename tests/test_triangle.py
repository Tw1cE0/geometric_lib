import unittest
from triangle import area, perimeter
class TestTriangle(unittest.TestCase):
    def test_perimeter_valid(self):
        self.assertEqual(perimeter(3, 4, 5), 12)
        self.assertEqual(perimeter(5, 12, 13), 30)

    def test_perimeter_invalid(self):
        with self.assertRaises(ValueError):
            perimeter(-3, 4, 5)
        with self.assertRaises(ValueError):
            perimeter(1, 1, 3)  # Violates triangle inequality
        with self.assertRaises(ValueError):
            perimeter(0, 4, 5)
        with self.assertRaises(ValueError):
            perimeter(3, 0, 5)
        with self.assertRaises(ValueError):
            perimeter(3, 4, 0)

    def test_area_valid(self):
        self.assertEqual(area(3, 4, 5), 6)
        self.assertAlmostEqual(area(5, 6, 7), 14.6969, places=4)

    def test_area_invalid(self):
        with self.assertRaises(ValueError):
            area(-3, 4, 5)
        with self.assertRaises(ValueError):
            area(1, 1, 3)  # Violates triangle inequality
        with self.assertRaises(ValueError):
            area(0, 4, 5)
        with self.assertRaises(ValueError):
            area(3, 0, 5)
        with self.assertRaises(ValueError):
            area(3, 4, 0)


if __name__ == '__main__':
    unittest.main()
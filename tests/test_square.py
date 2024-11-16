import unittest
from square import area, perimeter


class TestSquare(unittest.TestCase):
    def test_perimeter_positive(self):
        self.assertEqual(perimeter(5), 20)
        self.assertEqual(perimeter(10.5), 42)

    def test_perimeter_edge_cases(self):
        self.assertEqual(perimeter(0), 0)
        self.assertEqual(perimeter(0.001), 0.004)

    def test_perimeter_negative(self):
        with self.assertRaises(ValueError):
            perimeter(-5)
        with self.assertRaises(ValueError):
            perimeter(-0.1)

    def test_area_positive(self):
        self.assertEqual(area(5), 25)
        self.assertEqual(area(10.5), 110.25)

    def test_area_edge_cases(self):
        self.assertEqual(area(0), 0)
        self.assertEqual(area(0.001), 0.000001)

    def test_area_negative(self):
        with self.assertRaises(ValueError):
            area(-5)
        with self.assertRaises(ValueError):
            area(-0.1)


if __name__ == '__main__':
    unittest.main()

import unittest
import calculate
import math


class TestCalculate(unittest.TestCase):
    def test_circle_perimeter_valid(self):
        result = calculate.calc("circle", "perimeter", 5)
        self.assertAlmostEqual(result["perimeter"], 2 * math.pi * 5, places=5)

    def test_circle_area_valid(self):
        result = calculate.calc("circle", "area", 5)
        self.assertAlmostEqual(result["area"], math.pi * 5**2, places=5)

    def test_square_perimeter_valid(self):
        result = calculate.calc("square", "perimeter", 5)
        self.assertEqual(result["perimeter"], 20)

    def test_square_area_valid(self):
        result = calculate.calc("square", "area", 5)
        self.assertEqual(result["area"], 25)

    def test_invalid_figure_type(self):
        result = calculate.calc("triangle", "perimeter", 3, 4, 5)
        self.assertEqual(result["error"], "Неверный тип фигуры или имя функции")

    def test_invalid_function_name(self):
        result = calculate.calc("circle", "volume", 5)
        self.assertEqual(result["error"], "Неверный тип фигуры или имя функции")

    def test_invalid_size_count(self):
        result = calculate.calc("circle", "perimeter", 5, 10)
        self.assertEqual(result["error"], "Неверное количество аргументов")


if __name__ == '__main__':
    unittest.main()

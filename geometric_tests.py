import unittest
import math

from circle import area as circle_area, perimeter as circle_perimeter
from rectangle import area as rectangle_area, perimeter as rectangle_perimeter
from square import area as square_area, perimeter as square_perimeter
from triangle import area as triangle_area, perimeter as triangle_perimeter


class TestCircleExtended(unittest.TestCase):
    """Тестирование функций для круга"""

    def test_area_normal(self):
        """Тест площади круга с нормальными значениями"""
        self.assertAlmostEqual(circle_area(1), math.pi)
        self.assertAlmostEqual(circle_area(2.5), math.pi * 2.5 * 2.5)
        self.assertAlmostEqual(circle_area(0), 0)


    def test_perimeter_normal(self):
        """Тест периметра круга с нормальными значениями"""
        self.assertAlmostEqual(circle_perimeter(1), 2 * math.pi)
        self.assertAlmostEqual(circle_perimeter(3.14), 2 * math.pi * 3.14)
        self.assertAlmostEqual(circle_perimeter(0), 0)


    def test_area_negative_radius(self):
        """Тест площади круга с отрицательным радиусом"""
        with self.assertRaises(ValueError):
            circle_area(-1)


    def test_perimeter_negative_radius(self):
        """Тест периметра круга с отрицательным радиусом"""
        with self.assertRaises(ValueError):
            circle_perimeter(-5)


    def test_area_invalid_type(self):
        """Тест площади круга с некорректным типом данных"""
        with self.assertRaises(TypeError):
            circle_area("радиус")
        with self.assertRaises(TypeError):
            circle_area([1, 2, 3])


    def test_perimeter_invalid_type(self):
        """Тест периметра круга с некорректным типом данных"""
        with self.assertRaises(TypeError):
            circle_perimeter(None)
        with self.assertRaises(TypeError):
            circle_perimeter({"radius": 5})


class TestRectangleExtended(unittest.TestCase):
    """Тестирование функций для прямоугольника"""

    def test_area_normal(self):
        """Тест площади прямоугольника с нормальными значениями"""
        self.assertEqual(rectangle_area(5, 4), 20)
        self.assertAlmostEqual(rectangle_area(2.5, 3.5), 8.75)
        self.assertEqual(rectangle_area(0, 10), 0)
        self.assertEqual(rectangle_area(5, 0), 0)


    def test_perimeter_normal(self):
        """Тест периметра прямоугольника с нормальными значениями"""
        self.assertEqual(rectangle_perimeter(5, 4), 18)
        self.assertAlmostEqual(rectangle_perimeter(2.5, 3.5), 12.0)
        self.assertEqual(rectangle_perimeter(0, 10), 20)
        self.assertEqual(rectangle_perimeter(5, 0), 10)


    def test_area_negative_sides(self):
        """Тест площади прямоугольника с отрицательными сторонами"""
        with self.assertRaises(ValueError):
            rectangle_area(-5, 4)
        with self.assertRaises(ValueError):
            rectangle_area(5, -4)
        with self.assertRaises(ValueError):
            rectangle_area(-5, -4)


    def test_perimeter_negative_sides(self):
        """Тест периметра прямоугольника с отрицательными сторонами"""
        with self.assertRaises(ValueError):
            rectangle_perimeter(-5, 4)
        with self.assertRaises(ValueError):
            rectangle_perimeter(5, -4)
        with self.assertRaises(ValueError):
            rectangle_perimeter(-5, -4)


    def test_area_invalid_types(self):
        """Тест площади с некорректными типами данных"""
        with self.assertRaises(TypeError):
            rectangle_area("длина", 4)
        with self.assertRaises(TypeError):
            rectangle_area(5, [1, 2])


    def test_perimeter_invalid_types(self):
        """Тест периметра с некорректными типами данных"""
        with self.assertRaises(TypeError):
            rectangle_perimeter(5, "ширина")
        with self.assertRaises(TypeError):
            rectangle_perimeter(None, 4)


class TestSquareExtended(unittest.TestCase):
    """Тестирование функций для квадрата"""

    def test_area_normal(self):
        """Тест площади квадрата с нормальными значениями"""
        self.assertEqual(square_area(5), 25)
        self.assertAlmostEqual(square_area(2.5), 6.25)
        self.assertEqual(square_area(0), 0)


    def test_perimeter_normal(self):
        """Тест периметра квадрата с нормальными значениями"""
        self.assertEqual(square_perimeter(5), 20)
        self.assertAlmostEqual(square_perimeter(3.3), 13.2)
        self.assertEqual(square_perimeter(0), 0)


    def test_area_negative_side(self):
        """Тест площади квадрата с отрицательной стороной"""
        with self.assertRaises(ValueError):
            square_area(-5)


    def test_perimeter_negative_side(self):
        """Тест периметра квадрата с отрицательной стороной"""
        with self.assertRaises(ValueError):
            square_perimeter(-10)


    def test_area_invalid_type(self):
        """Тест площади квадрата с некорректным типом"""
        with self.assertRaises(TypeError):
            square_area("сторона")
        with self.assertRaises(TypeError):
            square_area((1, 2))


    def test_perimeter_invalid_type(self):
        """Тест периметра квадрата с некорректным типом"""
        with self.assertRaises(TypeError):
            square_perimeter({"side": 5})
        with self.assertRaises(TypeError):
            square_perimeter([5])


class TestTriangleExtended(unittest.TestCase):
    """Тестирование функций для треугольника"""

    def test_area_normal(self):
        """Тест площади треугольника с нормальными значениями"""
        self.assertEqual(triangle_area(10, 5), 25)
        self.assertEqual(triangle_area(0, 5), 0)
        self.assertEqual(triangle_area(10, 0), 0)


    def test_perimeter_normal(self):
        """Тест периметра треугольника с нормальными значениями"""
        self.assertEqual(triangle_perimeter(3, 4, 5), 12)
        self.assertAlmostEqual(triangle_perimeter(2.5, 3.5, 4.5), 10.5)
        self.assertEqual(triangle_perimeter(0, 4, 5), 9)
        self.assertEqual(triangle_perimeter(3, 0, 5), 8)
        self.assertEqual(triangle_perimeter(3, 4, 0), 7)


    def test_area_negative_values(self):
        """Тест площади треугольника с отрицательными значениями"""
        with self.assertRaises(ValueError):
            triangle_area(-10, 5)
        with self.assertRaises(ValueError):
            triangle_area(10, -5)
        with self.assertRaises(ValueError):
            triangle_area(-10, -5)


    def test_perimeter_negative_sides(self):
        """Тест периметра треугольника с отрицательными сторонами"""
        with self.assertRaises(ValueError):
            triangle_perimeter(-3, 4, 5)
        with self.assertRaises(ValueError):
            triangle_perimeter(3, -4, 5)
        with self.assertRaises(ValueError):
            triangle_perimeter(3, 4, -5)
        with self.assertRaises(ValueError):
            triangle_perimeter(-3, -4, -5)


    def test_area_invalid_types(self):
        """Тест площади треугольника с некорректными типами"""
        with self.assertRaises(TypeError):
            triangle_area("основание", 5)
        with self.assertRaises(TypeError):
            triangle_area(10, [5])


    def test_perimeter_invalid_types(self):
        """Тест периметра треугольника с некорректными типами"""
        with self.assertRaises(TypeError):
            triangle_perimeter(3, "сторона", 5)
        with self.assertRaises(TypeError):
            triangle_perimeter(3, 4, {"c": 5})



if __name__ == '__main__':
    unittest.main()
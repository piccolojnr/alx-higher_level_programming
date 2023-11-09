import unittest
from models.rectangle import Rectangle
from io import StringIO
import sys


class TestRectanle(unittest.TestCase):
    def test_str(self):
        # test __str__
        rect1 = Rectangle(4, 6, 2, 1, 12)

        self.assertEqual(str(rect1), "[Rectangle] (12) 2/1 - 4/6")
        print("run test_str successfully")

    def test_display(self):
        # Redirect stdout to capture the print output
        captured_output = StringIO()
        sys.stdout = captured_output

        # test display
        rect1 = Rectangle(4, 6, 2, 2)
        rect1.display()

        # reset redirect
        sys.stdout = sys.__stdout__

        # compare captured output to expected output
        expected_output = "\n\n  ####\n  ####\n  ####\n  ####\n  ####\n  ####\n"
        self.assertEqual(captured_output.getvalue(), expected_output)

        print("run test_display successfully")

    def test_area(self):
        # Test area method
        rect1 = Rectangle(4, 5)
        self.assertEqual(rect1.area(), 20)

        rect2 = Rectangle(3, 2)
        self.assertEqual(rect2.area(), 6)
        print("run test_area successfully")

    def test_width_validation(self):
        # Test valid width
        rect = Rectangle(4, 5)
        rect.width = 7
        self.assertEqual(rect.width, 7)

        # Test non-integer width
        with self.assertRaises(TypeError):
            rect.width = "invalid"

        # Test width <= 0
        with self.assertRaises(ValueError):
            rect.width = 0
        print("run test_width_validation successfully")

    def test_height_validation(self):
        # Test valid height
        rect = Rectangle(4, 5)
        rect.height = 8
        self.assertEqual(rect.height, 8)

        # Test non-integer height
        with self.assertRaises(TypeError):
            rect.height = "invalid"

        # Test height <= 0
        with self.assertRaises(ValueError):
            rect.height = -1
        print("run test_height_validation successfully")

    def test_x_validation(self):
        # Test valid x
        rect = Rectangle(4, 5)
        rect.x = 2
        self.assertEqual(rect.x, 2)

        # Test non-integer x
        with self.assertRaises(TypeError):
            rect.x = "invalid"

        # Test x < 0
        with self.assertRaises(ValueError):
            rect.x = -3
        print("run test_x_validation successfully")

    def test_y_validation(self):
        # Test valid y
        rect = Rectangle(4, 5)
        rect.y = 3
        self.assertEqual(rect.y, 3)

        # Test non-integer y
        with self.assertRaises(TypeError):
            rect.y = "invalid"

        # Test y < 0
        with self.assertRaises(ValueError):
            rect.y = -2
        print("run test_y_validation successfully")

    def test_constructor(self):
        # Test constructor without id
        rect1 = Rectangle(4, 5, 1, 2)
        self.assertEqual(rect1.id, 5)
        self.assertEqual(rect1.width, 4)
        self.assertEqual(rect1.height, 5)
        self.assertEqual(rect1.x, 1)
        self.assertEqual(rect1.y, 2)

        # Test constructor with id
        rect2 = Rectangle(2, 3, id=5)
        self.assertEqual(rect2.id, 5)
        self.assertEqual(rect2.width, 2)
        self.assertEqual(rect2.height, 3)
        self.assertEqual(rect2.x, 0)
        self.assertEqual(rect2.y, 0)
        print("run test_constructor successfully")


if __name__ == "__main__":
    unittest.main()

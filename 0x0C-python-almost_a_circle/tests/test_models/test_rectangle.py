import unittest
from models.rectangle import Rectangle
from io import StringIO
import sys


class TestRectangle(unittest.TestCase):
    def test_no_id(self):
        r1 = Rectangle(1, 2)
        r2 = Rectangle(1, 2)

        self.assertEqual(r1.id, r2.id - 1)
        self.assertEqual(r2.id, r1.id + 1)

        r3 = Rectangle(1, 2, 3)
        r4 = Rectangle(1, 2, 3)

        self.assertEqual(r3.id, r4.id - 1)
        self.assertEqual(r4.id, r3.id + 1)

    def test_type_error(self):
        with self.assertRaises(TypeError):
            Rectangle("1", 2)

        with self.assertRaises(TypeError):
            Rectangle(1, "2")

        with self.assertRaises(TypeError):
            Rectangle(1, 2, "3")

        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, "4")

    def test_value_error(self):
        with self.assertRaises(ValueError):
            Rectangle(-1, 2)

        with self.assertRaises(ValueError):
            Rectangle(0, 2)

        with self.assertRaises(ValueError):
            Rectangle(1, -2)

        with self.assertRaises(ValueError):
            Rectangle(1, 0)
        with self.assertRaises(ValueError):
            Rectangle(1, 2, -3)

        with self.assertRaises(ValueError):
            Rectangle(1, 2, 3, -4)

    def test_to_dictionary(self):
        r1 = Rectangle(10, 2, 1, 9, 1)

        r1_dictionary = r1.to_dictionary()
        self.assertEqual(
            r1_dictionary, {"id": 1, "height": 2, "width": 10, "x": 1, "y": 9}
        )

        r2 = Rectangle(1, 1)
        r2.update(**r1_dictionary)
        self.assertEqual(str(r1), str(r2))

    def test_update_kwargs(self):
        r1 = Rectangle(10, 10, 10, 10, 1)
        self.assertEqual(r1.id, 1)

        r1.update(height=1)
        self.assertEqual(r1.height, 1)
        r1.update(width=1, x=2)
        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.x, 2)
        r1.update(y=1, width=2, x=3, id=89)
        self.assertEqual(r1.id, 89)
        self.assertEqual(r1.y, 1)

    def test_update_args(self):
        r1 = Rectangle(10, 10, 10, 10, 1)

        self.assertEqual(r1.id, 1)

        r1.update(89)
        self.assertEqual(r1.id, 89)
        r1.update(89, 2)
        self.assertEqual(r1.width, 2)
        r1.update(89, 2, 3)
        self.assertEqual(r1.height, 3)
        r1.update(89, 2, 3, 4)
        self.assertEqual(r1.x, 4)
        r1.update(89, 2, 3, 4, 5)
        self.assertEqual(r1.y, 5)

    def test_str(self):
        # test __str__
        rect1 = Rectangle(4, 6, 2, 1, 12)

        self.assertEqual(str(rect1), "[Rectangle] (12) 2/1 - 4/6")

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
        e_out = "\n\n  ####\n  ####\n  ####\n  ####\n  ####\n  ####\n"
        self.assertEqual(captured_output.getvalue(), e_out)

    def test_display_no_x_and_y(self):
        # Redirect stdout to capture the print output
        captured_output = StringIO()
        sys.stdout = captured_output

        # test display
        rect1 = Rectangle(4, 6)
        rect1.display()

        # reset redirect
        sys.stdout = sys.__stdout__

        # compare captured output to expected output
        expected_output = "####\n####\n####\n####\n####\n####\n"
        self.assertEqual(captured_output.getvalue(), expected_output)

    def test_display_no_y(self):
        # Redirect stdout to capture the print output
        captured_output = StringIO()
        sys.stdout = captured_output

        # test display
        rect1 = Rectangle(4, 6, 2)
        rect1.display()

        # reset redirect
        sys.stdout = sys.__stdout__

        # compare captured output to expected output
        expected_output = "  ####\n  ####\n  ####\n  ####\n  ####\n  ####\n"
        self.assertEqual(captured_output.getvalue(), expected_output)

    def test_area(self):
        # Test area method
        rect1 = Rectangle(4, 5)
        self.assertEqual(rect1.area(), 20)

        rect2 = Rectangle(3, 2)
        self.assertEqual(rect2.area(), 6)

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


if __name__ == "__main__":
    unittest.main()

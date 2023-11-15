import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import os


class TestBase_Constructor(unittest.TestCase):
    def test_no_arg(self):
        b1 = Base()
        b2 = Base()
        b3 = Base()

        self.assertEqual(b1.id, b2.id - 1)
        self.assertEqual(b2.id, b1.id + 1)
        self.assertEqual(b3.id, b2.id + 1)

    def test_public_id(self):
        b = Base(12)
        b.id = 33
        self.assertEqual(b.id, 33)

    def test_one_arg(self):
        b = Base(0)
        self.assertEqual(b.id, 0)

    def test_neg_id(self):
        b = Base(-1)
        self.assertEqual(b.id, -1)

    def test_float_id(self):
        self.assertEqual(5.5, Base(5.5).id)

        b = Base(float("inf"))
        self.assertEqual(b.id, float("inf"))

        b = Base(float("-inf"))
        self.assertEqual(b.id, float("-inf"))

        b = Base(float("nan"))
        self.assertNotEqual(b.id, float("nan"))

    def test_bool_id(self):
        b = Base(True)
        self.assertEqual(b.id, True)

        b = Base(False)
        self.assertEqual(b.id, False)

    def test_list_id(self):
        b = Base([1, 2, 3])
        self.assertEqual(b.id, [1, 2, 3])

    def test_tuple_id(self):
        b = Base((1, 2, 3))
        self.assertEqual(b.id, (1, 2, 3))


class TestBase_methods(unittest.TestCase):
    def test_docstrings(self):
        self.assertIsNotNone(Base.__doc__)
        self.assertIs(hasattr(Base, "__init__"), True)
        self.assertIsNotNone(Base.__init__.__doc__)
        self.assertIs(hasattr(Base, "create"), True)
        self.assertIsNotNone(Base.create.__doc__)
        self.assertIs(hasattr(Base, "to_json_string"), True)
        self.assertIsNotNone(Base.to_json_string.__doc__)
        self.assertIs(hasattr(Base, "from_json_string"), True)
        self.assertIsNotNone(Base.from_json_string.__doc__)
        self.assertIs(hasattr(Base, "save_to_file"), True)
        self.assertIsNotNone(Base.save_to_file.__doc__)
        self.assertIs(hasattr(Base, "load_from_file"), True)
        self.assertIsNotNone(Base.load_from_file.__doc__)

    def tearDown(self) -> None:
        """delete any created files"""
        try:
            os.remove("Rectangle.json")
        except IOError:
            pass
        try:
            os.remove("Square.json")
        except IOError:
            pass
        try:
            os.remove("Rectangle.csv")
        except IOError:
            pass
        try:
            os.remove("Square.csv")
        except IOError:
            pass
        try:
            os.remove("Base.csv")
        except IOError:
            pass

    def test_save_to_file_csv_rectangle(self):
        r1 = Rectangle(10, 7, 2, 8, 5)
        r2 = Rectangle(2, 4, 1, 2, 3)
        Rectangle.save_to_file_csv([r1, r2])
        with open("Rectangle.csv", "r") as f:
            self.assertTrue("5,10,7,2,8\n2,4,1,2,3", f.read())

    def test_save_to_file_csv_square(self):
        s1 = Square(10, 7, 2, 8)
        s2 = Square(8, 1, 2, 3)
        Square.save_to_file_csv([s1, s2])
        with open("Square.csv", "r") as f:
            self.assertTrue("8,10,7,2\n3,8,1,2", f.read())

    def test_load_from_file_rectangle(self):
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        list_rectangles_output = Rectangle.load_from_file()
        self.assertEqual(type(list_rectangles_output), list)
        self.assertNotEqual(list_rectangles_output, [])

        for r_input, r_output in zip([r1, r2], list_rectangles_output):
            self.assertEqual(r_input.to_dictionary(), r_output.to_dictionary())

        self.assertTrue(
            all(isinstance(obj, Rectangle) for obj in list_rectangles_output)
        )

    def test_load_from_file_square(self):
        r1 = Square(10, 7, 2, 8)
        r2 = Square(2, 4, 4, 4)
        Square.save_to_file([r1, r2])
        list_sq_output = Square.load_from_file()

        self.assertEqual(type(list_sq_output), list)
        self.assertNotEqual(list_sq_output, [])

        for r_input, r_output in zip([r1, r2], list_sq_output):
            self.assertEqual(r_input.to_dictionary(), r_output.to_dictionary())

        self.assertTrue(all(isinstance(obj, Square) for obj in list_sq_output))

    def test_load_from_file_no_file(self):
        output = Square.load_from_file()
        self.assertEqual([], output)

    def test_load_from_file_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Base.load_from_file([], 1)

    def test_create(self):
        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual(r1 is r2, False)
        self.assertEqual(r1 == r2, False)
        self.assertEqual(r1.to_dictionary(), r2.to_dictionary())

    def test_save_to_file(self):
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", "r") as file:
            content = file.read()
        self.assertEqual(
            content,
            (
                '[{"id": 1, "width": 10, "height": 7, "x": 2, "y": 8}, '
                '{"id": 2, "width": 2, "height": 4, "x": 5, "y": 6}]'
            ),
        )

    def test_save_to_file_no_arg(self):
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as file:
            content = file.read()
        self.assertEqual(
            content,
            ("[]"),
        )

        Square.save_to_file(None)
        with open("Square.json", "r") as file:
            content = file.read()
        self.assertEqual(
            content,
            ("[]"),
        )

    def test_save_to_file_empty(self):
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as file:
            content = file.read()
        self.assertEqual(
            content,
            ("[]"),
        )

        Square.save_to_file([])
        with open("Square.json", "r") as file:
            content = file.read()
        self.assertEqual(
            content,
            ("[]"),
        )

    def test_from_json_string(self):
        list_input = [
            {"id": 89, "width": 10, "height": 4},
            {"id": 7, "width": 1, "height": 7},
        ]

        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(type(list_input), list)
        self.assertEqual(type(json_list_input), str)
        self.assertEqual(type(list_output), list)
        self.assertEqual(list_input, list_output)

        json_string = (
            '[{"id": 1, "width": 10, "height": 7, "x": 2, "y": 8},'
            '{"id": 2, "width": 2, "height": 3, "x": 3, "y": 4}]'
        )
        dictionary = Base.from_json_string(json_string)
        self.assertEqual(type(dictionary), list)
        self.assertEqual(
            dictionary,
            [
                {"id": 1, "width": 10, "height": 7, "x": 2, "y": 8},
                {"id": 2, "width": 2, "height": 3, "x": 3, "y": 4},
            ],
        )
        self.assertEqual(Base.from_json_string(None), [])
        self.assertEqual(Base.from_json_string(""), [])
        self.assertEqual(Base.from_json_string("[]"), [])
        self.assertEqual(Base.from_json_string("[{}]"), [{}])

    def test_to_json_string(self):
        r1 = Rectangle(10, 7, 2, 8, 1)
        dictionary = r1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        self.assertEqual(type(dictionary), dict)
        self.assertEqual(type(json_dictionary), str)
        self.assertEqual(
            json_dictionary,
            ('[{"id": 1, "width": 10, "height": 7, "x": 2, "y": 8}]'),
        )
        self.assertEqual(Base.to_json_string(None), "[]")
        self.assertEqual(Base.to_json_string([]), "[]")
        self.assertEqual(Base.to_json_string([{}]), "[{}]")
        self.assertEqual(Base.to_json_string([{"id": 1}]), '[{"id": 1}]')
        self.assertEqual(
            Base.to_json_string([{"id": 1, "width": 10}]),
            ('[{"id": 1, "width": 10}]'),
        )


if __name__ == "__main__":
    unittest.main()

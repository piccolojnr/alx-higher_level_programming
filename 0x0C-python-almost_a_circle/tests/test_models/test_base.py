import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestBase(unittest.TestCase):
    def test_load_from_file(self):
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        list_rectangles_output = Rectangle.load_from_file()
        self.assertEqual(type(list_rectangles_output), list)
        self.assertNotEqual(list_rectangles_output, [])

        for r_input, r_output in zip([r1, r2], list_rectangles_output):
            self.assertEqual(r_input.to_dictionary(), r_output.to_dictionary())

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
            '[{"id": 1, "width": 10, "height": 7, "x": 2, "y": 8}, {"id": 2, "width": 2, "height": 4, "x": 5, "y": 6}]',
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

        json_string = '[{"id": 1, "width": 10, "height": 7, "x": 2, "y": 8}, {"id": 2, "width": 2, "height": 3, "x": 3, "y": 4}]'
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
            json_dictionary, '[{"id": 1, "width": 10, "height": 7, "x": 2, "y": 8}]'
        )
        self.assertEqual(Base.to_json_string(None), "[]")
        self.assertEqual(Base.to_json_string([]), "[]")
        self.assertEqual(Base.to_json_string([{}]), "[{}]")
        self.assertEqual(Base.to_json_string([{"id": 1}]), '[{"id": 1}]')
        self.assertEqual(
            Base.to_json_string([{"id": 1, "width": 10}]), '[{"id": 1, "width": 10}]'
        )

    def test_id_incrementation(self):
        # Create two instances of Base without providing an id
        obj1 = Base()
        obj2 = Base()

        # Check if the ids are incremented correctly
        self.assertEqual(obj1.id, 3)
        self.assertEqual(obj2.id, 4)

    def test_id_assignment(self):
        # Create an instance of Base with a provided id
        obj = Base(id=5)

        # Check if the id is assigned correctly
        self.assertEqual(obj.id, 5)


if __name__ == "__main__":
    unittest.main()

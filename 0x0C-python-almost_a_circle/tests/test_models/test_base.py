import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestBase(unittest.TestCase):
    def test_to_json_string(self):
        r1 = Rectangle(10, 7, 2, 8, 1)
        dictionary = r1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        self.assertEqual(type(dictionary), dict)
        self.assertEqual(type(json_dictionary), str)
        self.assertEqual(
            json_dictionary, '[{"id": 1, "width": 10, "height": 7, "x": 2, "y": 8}]'
        )

    def test_id_incrementation(self):
        # Create two instances of Base without providing an id
        obj1 = Base()
        obj2 = Base()

        # Check if the ids are incremented correctly
        self.assertEqual(obj1.id, 1)
        self.assertEqual(obj2.id, 2)

    def test_id_assignment(self):
        # Create an instance of Base with a provided id
        obj = Base(id=5)

        # Check if the id is assigned correctly
        self.assertEqual(obj.id, 5)


if __name__ == "__main__":
    unittest.main()

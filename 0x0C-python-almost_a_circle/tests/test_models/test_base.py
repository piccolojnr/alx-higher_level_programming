import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    def test_id_incrementation(self):
        # Create two instances of Base without providing an id
        obj1 = Base()
        obj2 = Base()

        # Check if the ids are incremented correctly
        self.assertEqual(obj1.id, 1)
        self.assertEqual(obj2.id, 2)
        print("run test_id_incrementation successfully")

    def test_id_assignment(self):
        # Create an instance of Base with a provided id
        obj = Base(id=5)

        # Check if the id is assigned correctly
        self.assertEqual(obj.id, 5)
        print("run test_id_assignment successfully")


if __name__ == "__main__":
    unittest.main()

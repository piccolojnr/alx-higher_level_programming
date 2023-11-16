import unittest
from models.square import Square


class TestRectanle(unittest.TestCase):
    def test_to_dictionary(self):
        sq1 = Square(10, 2, 1, 1)

        sq1_dictionary = sq1.to_dictionary()
        self.assertEqual(sq1_dictionary, {"id": 1, "size": 10, "x": 2, "y": 1})

        sq2 = Square(1, 1)
        sq2.update(**sq1_dictionary)
        self.assertEqual(str(sq1), str(sq2))

    def test_update(self):
        sq1 = Square(4)
        sq1.update(10, 10, 10, 10)
        self.assertEqual(sq1.id, 10)
        self.assertEqual(sq1.size, 10)
        self.assertEqual(sq1.x, 10)
        self.assertEqual(sq1.y, 10)

        sq2 = Square(4)
        self.assertEqual(sq2.size, 4)

        sq2.update(size=10)
        self.assertEqual(sq2.size, 10)

        sq2.update(x=1)
        self.assertEqual(sq2.x, 1)

        sq2.update(size=7, id=89)
        self.assertEqual(sq2.size, 7)
        self.assertEqual(sq2.id, 89)

        sq2.update()
        self.assertEqual(sq2.size, 7)
        self.assertEqual(sq2.id, 89)

        sq2.update(id=1, size=2)
        self.assertEqual(sq2.id, 1)
        self.assertEqual(sq2.size, 2)

    def test_size(self):
        sq = Square(4)
        self.assertEqual(sq.size, 4)

        sq.size = 10
        self.assertEqual(sq.size, 10)

        with self.assertRaises(TypeError):
            sq.size = "5"

    def test_square_exists(self):
        sq1 = Square(1, 2)
        sq2 = Square(1, 2)

        self.assertEqual(sq1.id, sq2.id - 1)
        self.assertEqual(sq2.id, sq1.id + 1)

        sq1 = Square(1, 2, 3)
        sq2 = Square(1, 2, 3)

        self.assertEqual(sq1.id, sq2.id - 1)
        self.assertEqual(sq2.id, sq1.id + 1)

    def test_type_error(self):
        with self.assertRaises(TypeError):
            Square("1")

        with self.assertRaises(TypeError):
            Square(1, "2")

        with self.assertRaises(TypeError):
            Square(1, 2, "3")

        with self.assertRaises(ValueError):
            Square(-1)

        with self.assertRaises(ValueError):
            Square(1, -2)

        with self.assertRaises(ValueError):
            Square(1, 2, -3)

        with self.assertRaises(ValueError):
            Square(0)

    def test_str_exists(self):
        sq = Square(1, 2, 3, 4)
        self.assertEqual(str(sq), "[Square] (4) 2/3 - 1")
        sq.size = 10
        self.assertEqual(str(sq), "[Square] (4) 2/3 - 10")
        sq.x = 5
        self.assertEqual(str(sq), "[Square] (4) 5/3 - 10")
        sq.y = 6
        self.assertEqual(str(sq), "[Square] (4) 5/6 - 10")
        sq.id = 7
        self.assertEqual(str(sq), "[Square] (7) 5/6 - 10")
        sq.size = 11
        self.assertEqual(str(sq), "[Square] (7) 5/6 - 11")
        sq.x = 12
        self.assertEqual(str(sq), "[Square] (7) 12/6 - 11")
        sq.y = 13
        self.assertEqual(str(sq), "[Square] (7) 12/13 - 11")
        sq.id = 8

    def test_square_existence(self):
        square_instance = Square(1, 2, 3)

        self.assertIsInstance(square_instance, Square)
        self.assertEqual(square_instance.x, 2)
        self.assertEqual(square_instance.y, 3)
        self.assertEqual(square_instance.size, 1)

        sq1 = Square(1, 2, 3)
        sq2 = Square(1, 2, 3)

        self.assertEqual(sq1.id, sq2.id - 1)
        self.assertEqual(sq2.id, sq1.id + 1)


if __name__ == "__main__":
    unittest.main()

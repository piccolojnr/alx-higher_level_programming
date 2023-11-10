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


if __name__ == "__main__":
    unittest.main()

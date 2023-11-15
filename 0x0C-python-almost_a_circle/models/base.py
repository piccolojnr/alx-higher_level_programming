#!/usr/bin/python3

"""Module documentation for the base module."""

import json
import csv
import turtle


class Base:
    """Base class for other classes in the project."""

    __nb_objects = 0

    def __init__(self, id=None):
        """
        init
        Args:
            id (int): id of the Base
        Returns:
            None
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """to_json_string"""
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """save_to_file"""
        with open(cls.__name__ + ".json", "w") as f:
            if list_objs is None:
                f.write("[]")
            else:
                list_dicts = [o.to_dictionary() for o in list_objs]
                f.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """
        from_json_string
        Returns:
            list: list of instances
        """
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        create
        Returns:
            instance: instance of the class
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """
        load_from_file
        Returns:
            list: list of instances
        """
        try:
            with open(cls.__name__ + ".json", "r") as f:
                return [cls.create(**d) for d in cls.from_json_string(f.read())]
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        save_to_file_csv
        Args:
            list_objs: list of instances
        Returns:
            None: None. (void function)
        """
        with open(cls.__name__ + ".csv", mode="w", newline="") as f:
            writer = csv.writer(f)
            for obj in list_objs:
                if cls.__name__ == "Rectangle":
                    writer.writerow([obj.width, obj.height, obj.x, obj.y])
                elif cls.__name__ == "Square":
                    writer.writerow([obj.size, obj.x, obj.y])

    @classmethod
    def load_from_file_csv(cls):
        """
        load_from_file_csv
        Returns:
            list: list of instances
        """
        try:
            result = []
            with open(cls.__name__ + ".csv", "r") as f:
                reader = csv.reader(f)
                for row in reader:
                    row = list(map(int, row))
                    if cls.__name__ == "Rectangle":
                        d = {
                            "width": row[0],
                            "height": row[1],
                            "x": row[2],
                            "y": row[3],
                        }
                    elif cls.__name__ == "Square":
                        d = {"size": row[0], "x": row[1], "y": row[2]}

                    result.append(cls.create(**d))
                return result
        except FileNotFoundError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """draw
        Args:
            list_rectangles: list of rectangles
            list_squares: list of squares
        Returns:
            None: None. (void function)
        """
        pen = turtle.Turtle()
        pen.screen.bgcolor("black")
        pen.pensize(3)
        pen.shape("turtle")

        pen.color("white")
        for rect in list_rectangles:
            pen.showturtle()
            pen.up()
            pen.goto(rect.x, rect.y)
            pen.down()
            for i in range(2):
                pen.forward(rect.width)
                pen.left(90)
                pen.forward(rect.height)
                pen.left(90)

        pen.color("red")
        for sq in list_squares:
            pen.up()
            pen.showturtle()
            pen.goto(sq.x, sq.y)
            pen.down()
            for i in range(2):
                pen.forward(sq.size)
                pen.left(90)
                pen.forward(sq.size)
                pen.left(90)

        turtle.exitonclick()
        return None

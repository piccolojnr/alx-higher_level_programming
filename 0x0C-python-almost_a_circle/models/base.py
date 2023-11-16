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
                ls = []
                for d in cls.from_json_string(f.read()):
                    ls.append(cls.create(**d))
                return ls
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
        filename = cls.__name__ + ".csv"
        with open(filename, mode="w", newline="") as file:
            writer = csv.writer(file)
            for obj in list_objs:
                if cls.__name__ == "Rectangle":
                    writer.writerow([obj.id, obj.width, obj.height, obj.x, obj.y])
                elif cls.__name__ == "Square":
                    writer.writerow([obj.id, obj.size, obj.x, obj.y])

    @classmethod
    def load_from_file_csv(cls):
        """
        load_from_file_csv
        Returns:
            list: list of instances
        """
        try:
            filename = cls.__name__ + ".csv"
            result = []
            with open(filename, mode="r") as file:
                reader = csv.reader(file)
                for row in reader:
                    row = list(map(int, row))
                    if cls.__name__ == "Rectangle":
                        result.append(cls(row[1], row[2], row[3], row[4], row[0]))
                    elif cls.__name__ == "Square":
                        result.append(cls(row[1], row[2], row[3], row[0]))
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

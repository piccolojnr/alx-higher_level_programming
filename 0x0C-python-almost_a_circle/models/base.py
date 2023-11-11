#!/usr/bin/python3
import json
import csv
import tkinter as tk


"""Base class"""


class Base:
    """Base class"""

    __nb_objects = 0

    def __init__(self, id=None):
        """init"""
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
        """from_json_string"""
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """create"""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """load_from_file"""
        try:
            with open(cls.__name__ + ".json", "r") as f:
                return [cls.create(**d) for d in cls.from_json_string(f.read())]
        except:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """save_to_file_csv"""
        with open(cls.__name__ + ".csv", mode="w", newline="") as f:
            writer = csv.writer(f)
            for obj in list_objs:
                if cls.__name__ == "Rectangle":
                    writer.writerow([obj.width, obj.height, obj.x, obj.y])
                elif cls.__name__ == "Square":
                    writer.writerow([obj.size, obj.x, obj.y])

    @classmethod
    def load_from_file_csv(cls):
        """load_from_file_csv"""
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
        except:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """draw"""

        root = tk.Tk()
        root.title("Drawing")
        root.minsize(600, 600)
        canvas = tk.Canvas(root, width=600, height=600)
        canvas.pack()
        for rect in list_rectangles:
            canvas.create_rectangle(
                rect.x,
                rect.y,
                rect.x + rect.width,
                rect.y + rect.height,
            )
        for sq in list_squares:
            canvas.create_rectangle(
                sq.x,
                sq.y,
                sq.x + sq.size,
                sq.y + sq.size,
            )
        root.mainloop()
        return None

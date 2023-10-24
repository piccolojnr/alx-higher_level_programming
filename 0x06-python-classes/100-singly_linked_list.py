#!/usr/bin/python3
"""Define a singly linked list"""


class Node:
    """class of a single node"""

    def __init__(self, data, next_node=None):
        """Initialize attributes"""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """get the data of node"""
        return self.__data

    @data.setter
    def data(self, value):
        """set data of node"""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        """get next node"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """set next node"""

        if value is None or isinstance(value, Node):
            self.__next_node = value
        else:
            raise TypeError("next_node must be a Node object")


class SinglyLinkedList:
    """class of a singly linked list"""

    def __init__(self):
        """Initialize attributes"""
        self.__head = None

    def sorted_insert(self, value):
        """insert a new node in sorted way"""
        new_node = Node(value)
        if self.__head is None:
            self.__head = new_node
        elif self.__head.data > value:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            tmp = self.__head
            while tmp.next_node is not None and tmp.next_node.data < value:
                tmp = tmp.next_node
            new_node.next_node = tmp.next_node
            tmp.next_node = new_node

    def __str__(self):
        """print the linked list"""
        tmp = self.__head
        result = ""
        while tmp is not None:
            result += str(tmp.data) + "\n"
            tmp = tmp.next_node
        return result[:-1]

#!/usr/bin/python3
"""
 MyInt is a rebel. MyInt has == and != operators inverted
"""


class MyInt(int):
    """
    MyInt is a rebel. MyInt has == and != operators inverted
    """

    def __eq__(self, __value: object) -> bool:
        """
        __eq__ inverted.
        Args:
            __value: object
        Returns:
            bool: inverted __eq__
        Raises:
            None.
        """
        return super().__ne__(__value)

    def __ne__(self, __value: object) -> bool:
        """
        __ne__ inverted.
        Args:
            __value: object
        Returns:
            bool: inverted __ne__
        Raises:
            None.
        """
        return super().__eq__(__value)

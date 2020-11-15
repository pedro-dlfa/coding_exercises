from collections import deque


class Stack:
    """ Stack structure

    Basic implementation of Stack data structure, where inserted items are stored at the end
    of the structure and removed items are deleted from the end of the data structure.
    """

    def __init__(self):
        self.__stack = deque()

    def push(self, item):
        """
        Stores the given item at the end of the stack
        """
        self.__stack.append(item)

    def pop(self):
        """
        Removes and returns the last element of the stack
        """
        return self.__stack.pop()

    def __contains__(self, item):
        return item in self.__stack

    def __repr__(self):
        return f"Stack: [{', '.join(str(e) for e in self.__stack)}]"

    def __str__(self):
        return repr(self)

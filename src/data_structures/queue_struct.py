from collections import deque


class Queue:
    """Queue structure

    Basic implementation of Queue data structure, where inserted items are stored at the end of the structure
    and removed items are deleted from the beginning of the data structure.
    """

    def __init__(self):
        self.__queue = deque()

    def enqueue(self, item):
        """
        Stores the given item at the end of the queue
        """
        self.__queue.append(item)

    def dequeue(self):
        """
        Removes and returns the first element of the queue
        """
        return self.__queue.popleft()

    def __contains__(self, item):
        return item in self.__queue

    def __repr__(self):
        return f"Queue: [{', '.join(str(e) for e in self.__queue)}]"

    def __str__(self):
        return repr(self)

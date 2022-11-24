# Synopsis:
#   Implements the Queue ADT
#
# A queue ( also called a FIFO queue ) is a compound data structure in which the data values are ordered according to
# the FIFO (first -in first -out) protocol.

class Queue(object):
    def __init__(self):
        """
        Purpose:
            Creates an empty queue.
        Return:
            An empty queue.
            """
        self.data = list()

    def is_empty(self):
        """
        Purpose:
            Checks if the given queue has no data in it.
        Return:
            True if the queue has no data, or false otherwise.
        """
        return len( self . data ) == 0

    def size(self):
        """
        Purpose:
            Returns the number of data values in the given queue.
        Return:
            The number of data values in the queue.
        """
        return len(self.data)

    def enqueue(self, value):
        """
        Purpose:
            Adds the given data value to the given queue.
        Pre-Conditions:
            Queue: A queue created by create().
            value: Data to be added.
        Post-Condition:
            The value is added to the queue.
        Return:
            (none)
        """
        self.data.append(value)

    def dequeue(self):
        """
        Purpose:
            Removes and returns a data value from the given queue.
        Pre-Conditions:
            Queue: A queue created by create().
        Post-Condition:
            The first value is removed from the queue.
        Return:
            The first value in the queue.
        """
        return self.data.pop(0)

    def peek(self):
        """
        Purpose:
            Returns the value from the front of given queue without removing it.
        Pre-Conditions:
            queue:a queue created by create().
        Post-Condition:
            (None)
        Return:
            The value at the front of the queue.
        """
        return self.data[0]
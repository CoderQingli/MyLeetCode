def __init__(self):
    """
    Initialize your data structure here.
    """
    self.s = []


def push(self, x):
    """
    Push element x to the back of queue.
    :type x: int
    :rtype: None
    """
    self.s.append(x)


def pop(self):
    """
    Removes the element from in front of queue and returns that element.
    :rtype: int
    """
    return self.s.pop(0)


def peek(self):
    """
    Get the front element.
    :rtype: int
    """
    return self.s[0]


def empty(self):
    """
    Returns whether the queue is empty.
    :rtype: bool
    """
    return self.s == []
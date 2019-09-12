def __init__(self):
    """
    initialize your data structure here.
    """
    self.res = []
    self.getmin = []


def push(self, x):
    """
    :type x: int
    :rtype: None
    """
    self.res.append(x)
    if not self.getmin or self.getmin[-1] >= x:
        self.getmin.append(x)


def pop(self):
    """
    :rtype: None
    """
    p = self.res.pop()
    if p == self.getmin[-1]:
        self.getmin.pop()


def top(self):
    """
    :rtype: int
    """
    return self.res[-1]


def getMin(self):
    """
    :rtype: int
    """
    return self.getmin[-1]  
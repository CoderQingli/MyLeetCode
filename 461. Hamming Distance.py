def hammingDistance(self, x, y):
    """
    :type x: int
    :type y: int
    :rtype: int
    """
    res = x ^ y
    return bin(res).count("1")
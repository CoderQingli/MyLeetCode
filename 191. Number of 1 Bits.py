def hammingWeight(self, n):
    """
    :type n: int
    :rtype: int
    """
    tmp = bin(n)
    return tmp.count("1")
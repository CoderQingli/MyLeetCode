def arrangeCoins(self, n):
    """
    :type n: int
    :rtype: int
    """
    res = (int((8 * n + 1) ** 0.5) - 1) // 2
    return res
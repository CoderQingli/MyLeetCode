def judgeSquareSum(self, c):
    """
    :type c: int
    :rtype: bool
    """
    l = 0
    r = int(c ** 0.5)
    while l <= r:
        if l ** 2 + r ** 2 == c:
            return True
        if l ** 2 + r ** 2 > c:
            r -= 1
        else:
            l += 1
    return False
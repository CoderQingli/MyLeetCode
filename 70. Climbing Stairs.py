def climbStairs(self, n):
    """
    :type n: int
    :rtype: int
    """
    res = [1, 2]
    while len(res) < n:
        res.append(res[-1] + res[-2])
    return res[n - 1]
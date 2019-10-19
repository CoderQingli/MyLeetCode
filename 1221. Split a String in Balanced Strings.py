def balancedStringSplit(self, S):
    """
    :type s: str
    :rtype: int
    """
    r = 0
    l = 0
    res = 0
    for s in S:
        if s == "R":
            r += 1
        else:
            l += 1
        if r == l:
            res += 1
    return res
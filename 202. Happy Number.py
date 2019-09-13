def isHappy(self, n):
    """
    :type n: int
    :rtype: bool
    """
    tmp = []
    while self.helper(n) != 1:
        n = self.helper(n)
        if n in tmp:
            return False
        tmp.append(n)
    return True


def helper(self, n):
    res = 0
    for i in str(n):
        res += int(i) ** 2
    return res
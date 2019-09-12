def convertToTitle(self, n):
    """
    :type n: int
    :rtype: str
    """
    res = []
    while n > 0:
        n, d = divmod(n - 1, 26)
        res.append(chr(ord('A') + d))
    return ''.join(res[::-1])
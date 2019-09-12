def trailingZeroes(self, n):
    """
    :type n: int
    :rtype: int
    """
    if n < 5:
        return 0
    cnt = 0
    while n != 0:
        cnt += n // 5
        n = n // 5
    return cnt
def isPowerOfThree(self, n):
    """
    :type n: int
    :rtype: bool
    """
    if n < 1:
        return False
    while n % 3 == 0:
        n //= 3
    if n == 1:
        return True
    return False
def isPowerOfFour(self, num):
    """
    :type num: int
    :rtype: bool
    """
    if num < 1:
        return False
    while num % 4 == 0:
        num //= 4
    if num == 1:
        return True
    return False
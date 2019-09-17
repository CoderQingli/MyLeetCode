def addDigits(self, num):
    """
    :type num: int
    :rtype: int
    """
    if num < 10:
        return num
    res = num % 9
    if res == 0:
        return 9
    else:
        return res
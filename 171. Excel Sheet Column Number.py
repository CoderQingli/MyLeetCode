def titleToNumber(self, s):
    """
    :type s: str
    :rtype: int
    """
    return sum([(ord(c) - 64) * 26 ** i for i, c in enumerate(s[::-1])])
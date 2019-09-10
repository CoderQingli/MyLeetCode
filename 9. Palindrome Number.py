def isPalindrome(self, x):
    """
    :type x: int
    :rtype: bool
    """
    if x < 0:
        return False
    rev = 0
    pre = x
    while x:
        rev = rev * 10 + x % 10
        x /= 10
    return rev == pre
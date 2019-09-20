def isPerfectSquare(self, num):
    """
    :type num: int
    :rtype: bool
    """
    l = 1
    r = num
    while l <= r:
        mid = (l + r) // 2
        if mid * mid == num:
            return True
        if mid * mid < num:
            l = mid + 1
        else:
            r = mid - 1
    return False 
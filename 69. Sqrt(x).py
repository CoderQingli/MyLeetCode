def mySqrt(self, x):
    """
    :type x: int
    :rtype: int
    """
    h = x
    l = 0
    while l <= h:
        mid = (l + h) // 2
        if mid * mid > x:
            h = mid - 1
        elif mid * mid < x:
            l = mid + 1
        else:
            return mid
    return h

def firstBadVersion(self, n):
    """
    :type n: int
    :rtype: int
    """
    if isBadVersion(1):
        return 1
    l = 1
    r = n
    while l < r - 1:
        mid = (l + r) // 2
        if isBadVersion(mid):
            r = mid
        else:
            l = mid
    return r
def guessNumber(self, n):
    """
    :type n: int
    :rtype: int
    """
    l = 1
    r = n
    while l <= r:
        ml = l + (r - l) / 3
        mr = r - (r - l) / 3
        gl = guess(ml)
        gr = guess(mr)
        if gl == 0:
            return ml
        if gr == 0:
            return mr
        elif gl < 0:
            r = ml - 1
        elif gr > 0:
            l = mr + 1
        else:
            l = ml + 1
            r = mr - 1
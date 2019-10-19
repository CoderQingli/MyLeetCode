def tribonacci(self, n):
    """
    :type n: int
    :rtype: int
    """
    t0, t1, t2 = 0, 1, 1
    if n < 3:
        if n == 1:
            return 1
        elif n == 2:
            return 1
        else:
            return 0
    for i in range(n - 2):
        tmp = t0 + t1 + t2
        t0, t1, t2 = t1, t2, tmp
    return tmp
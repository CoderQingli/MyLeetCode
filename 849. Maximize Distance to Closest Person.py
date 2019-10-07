def maxDistToClosest(self, seats):
    """
    :type seats: List[int]
    :rtype: int
    """
    firstone = seats.index(1)
    lastone = seats[::-1].index(1)
    tmp = 0
    cnt = 0
    for i in seats[firstone:(len(seats) - lastone)]:
        if i == 0:
            cnt += 1
        else:
            tmp = max(tmp, cnt)
            cnt = 0
    return max(firstone, lastone, (tmp + 1) / 2)
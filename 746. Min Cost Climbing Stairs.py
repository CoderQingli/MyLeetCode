def minCostClimbingStairs(self, cost):
    """
    :type cost: List[int]
    :rtype: int
    """
    s1 = s2 = 0
    for x in cost[::-1]:
        s1, s2 = x + min(s1, s2), s1
    return min(s1, s2)

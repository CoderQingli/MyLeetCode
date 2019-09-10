def maxProfit(self, prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    if len(prices) == 0 or len(prices) == 1:
        return 0
    res = 0
    minp = prices[0]
    for i in range(1, len(prices)):
        if prices[i] < minp:
            minp = prices[i]
        elif prices[i] - minp > res:
            res = prices[i] - minp
    return res
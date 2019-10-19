def distributeCandies(self, candies, num_people):
    """
    :type candies: int
    :type num_people: int
    :rtype: List[int]
    """
    res = [0] * num_people
    give = 1
    i = 0

    while candies > 0:
        if give <= candies:
            res[i] += give
        else:
            give = candies
            res[i] += candies
        candies -= give
        give += 1
        i += 1
        i = i % num_people
    return res
def twoCitySchedCost(self, costs):
    """
    :type costs: List[List[int]]
    :rtype: int
    """
    if not costs:
        return 0
    costs = sorted(costs, key=lambda l: l[0] - l[1])
    res = 0
    for i in range(len(costs) / 2):
        res += costs[i][0]
    for i in range(len(costs) / 2, len(costs)):
        res += costs[i][1]
    return res
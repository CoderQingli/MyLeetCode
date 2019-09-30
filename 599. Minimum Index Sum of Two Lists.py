def findRestaurant(self, list1, list2):
    """
    :type list1: List[str]
    :type list2: List[str]
    :rtype: List[str]
    """
    if not list1 or not list2:
        return []
    res = []
    tmp = 10000000
    for i in list1:
        if i in list2:
            if list1.index(i) + list2.index(i) <= tmp:
                res.append(i)
                tmp = list1.index(i) + list2.index(i)
    return res
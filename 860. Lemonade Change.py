def lemonadeChange(bills):
    """
    :type bills: List[int]
    :rtype: bool
    """
    res = {5: 0, 10: 0}
    for b in bills:
        if b == 5:
            res[5] += 1
        elif b == 10:
            if res[5] == 0:
                return False
            else:
                res[10] += 1
                res[5] -= 1
        else:
            if res[5] == 0:
                return False
            if res[10] != 0:
                res[5] -= 1
                res[10] -= 1
            else:
                res[5] -= 3
                if res[5] < 0:
                    return False
    return True
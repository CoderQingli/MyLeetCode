def commonChars(self, A):
    """
    :type A: List[str]
    :rtype: List[str]
    """
    tmp = ""
    res = []
    for a in A:
        tmp += a
    tmp = list(set(tmp))
    for c in tmp:
        cnt = [a.count(c) for a in A]
        if 0 in cnt:
            continue
        res += [c] * min(cnt)
    return res
def reverseOnlyLetters(self, S):
    """
    :type S: str
    :rtype: str
    """
    tmp = [t for t in S if t.isalpha()]
    res = []
    for c in S:
        if c.isalpha():
            res.append(tmp.pop())
        else:
            res.append(c)
    return "".join(res)